from django.shortcuts import render

import abacatepay
from django.conf import settings
from django.shortcuts import render
# from ingressos.models import Ingresso

# abacatepay.api_key = settings.ABACATEPAY_API_KEY

# def criar_cobranca(request):
#     if request.method == 'POST':
#         nome = request.POST['nome']
#         tipo = request.POST['tipo_ingresso']
#         valor = float(request.POST['valor'])

#         cobranca = abacatepay.billing.create({
#             "frequency": "ONE_TIME",
#             "methods": ["PIX"],
#             "products": [{
#                 "name": f"Ingresso {tipo}",
#                 "price": int(valor * 100)  # em centavos
#             }],
#             "customer": {
#                 "email": "teste@email.com"
#             }
#         })

#         ingresso = Ingresso.objects.create(
#             nome_cliente=nome,
#             tipo_ingresso=tipo,
#             valor=valor,
#             status_pagamento='pendente',
#             codigo_qr=cobranca["pix"]["qr_code_url"]
#         )

#         return render(request, 'pagamentos/pagamento.html', {'ingresso': ingresso})
#     return render(request, 'pagamentos/formulario.html')


def pagamento(request):
    return render (request, 'frontend/pagamento.html')

# # Create your views here.
