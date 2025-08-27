from django.shortcuts import render
import abacatepay
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, redirect
from ingressos.models import Ingresso
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.mail import send_mail
import json
import random 
import string
from bar.models import Produto, Pedido

abacatepay.api_key = settings.ABACATEPAY_API_KEY

def gerar_codigo_pulseira():
    return 'TOTEM-' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def iniciar_pagamento(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        email = request.POST['email']
        tipo = request.POST['tipo_ingresso']
        telefone = request.POST['telefone']

        
        if tipo == 'pista':
            produto_nome = 'ingresso_pista'
            preco = 12000
            descricao = 'ingresso tipo pista que tem limitações de áreas liberadas'
        else:
            produto_nome = 'ingresso_vip'
            preco = 20000
            descricao = 'ingresso tipo camarote com acesso exclusivo'

        payload = {
            "frequency": "ONE_TIME",
            "methods": ["PIX"],
            "allowCoupons": False,
            "coupons": [],
            "products": [
                {
                    "name": produto_nome,
                    "quantity": 1,
                    "externalId": produto_nome,
                    "price": preco,
                    "description": descricao
                }
            ],
            "returnUrl": f"https://{settings.NGROK_URL}/ingressos/cadastro/",
            "completionUrl": f"https://{settings.NGROK_URL}/",
            "customer": {
                "name": nome,
                "cellphone": telefone,  
                "email": email,
                "taxId": cpf
            }
        }

        headers = {
            "Authorization": f"Bearer {settings.ABACATEPAY_API_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.post("https://api.abacatepay.com/v1/billing/create", json=payload, headers=headers)

        if response.status_code == 200:
            dados = response.json()
            cobranca = dados.get("data", {})
            checkout_url = cobranca.get("url")
            id_cobranca = cobranca.get("id")

            if checkout_url and id_cobranca:
                
                Ingresso.objects.create(
                    nome_cliente=nome,
                    cpf=cpf,
                    email=email,
                    telefone=telefone,
                    tipo_ingresso=tipo,
                    valor=preco / 100,  
                    status_pagamento='pendente',
                    id_cobranca=id_cobranca,
                    codigo_pulseira = gerar_codigo_pulseira()
                )

                return redirect(checkout_url)
            else:
                return HttpResponse("Erro: URL ou ID da cobrança não encontrados.", status=500)
        else:
            return HttpResponse(f"Erro ao criar cobrança: {response.text}", status=400)

    return redirect('iniciar_pagamento')



@csrf_exempt
def confirmar_pagamento(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        print("Webhook recebido:", body)

        try:
            id_cobranca = body["data"]["billing"]["id"]
            status = body["data"]["billing"]["status"]
        except KeyError:
            return JsonResponse({"error": "Formato inválido"}, status=400)

        if status == "PAID":
            try:
                ingresso = Ingresso.objects.get(id_cobranca=id_cobranca)
                ingresso.status_pagamento = "pago"
                ingresso.save()
                # send_mail(
                #     subject='Seu ingresso foi confirmado!',
                #     message=f'Olá {ingresso.nome_cliente}, seu código de pulseira é: {ingresso.codigo_pulseira}',
                #     from_email='totemfestival1@gmail.com',
                #     recipient_list=[ingresso.email],
                #     fail_silently=False,
                # )

                return JsonResponse({"message": "Pagamento confirmado"})
            except Ingresso.DoesNotExist:
                return JsonResponse({"error": "Cobrança não encontrada"}, status=404)

        return JsonResponse({"message": "Status não é PAID"}, status=200)

    return JsonResponse({"error": "Método não permitido"}, status=405)



def iniciar_pagamento_produto(request, produto_id):
    if not request.session.get('usuario_id'):
        print("Sessão ativa:", request.session.get('usuario_id'))
        return HttpResponse("Você precisa estar registrado para comprar.", status=403)


    # usuario = Usuario.objects.get(id=request.session['usuario_id'])
    usuario = Ingresso.objects.get(id=request.session['usuario_id'])
    produto = Produto.objects.get(id=produto_id)

    payload = {
        "frequency": "ONE_TIME",
        "methods": ["PIX"],
        "products": [{
            "name": produto.nome,
            "quantity": 1,
            "externalId": f"produto_{produto.id}",
            "price": produto.preco * 100,
            "description": produto.descricao
        }],
        "returnUrl": f"https://{settings.NGROK_URL}/bar/",
        "completionUrl": f"https://{settings.NGROK_URL}/",
        "customer": {
            "name": usuario.nome_cliente,
            "cellphone": usuario.telefone,
            "email": usuario.email,
            "taxId": usuario.cpf
        }
    }

    headers = {
        "Authorization": f"Bearer {settings.ABACATEPAY_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post("https://api.abacatepay.com/v1/billing/create", json=payload, headers=headers)

    if response.status_code == 200:
        dados = response.json()["data"]
        
        Pedido.objects.create(
            usuario=usuario,
            produto=produto,
            id_cobranca=dados["id"],
            status_pagamento="pendente"
        )
        return redirect(dados["url"])###
    else:
        return HttpResponse("Erro ao iniciar pagamento", status=400)
