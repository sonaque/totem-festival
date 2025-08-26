from django.shortcuts import render, redirect
from .models import Produto
from ingressos.models import Ingresso

def pagina_bar(request):
    produtos = Produto.objects.filter(ativo=True)
    return render(request, 'frontend/bar.html', {'produtos': produtos})


# def registrar_pulseira(request):
#     if request.method == 'POST':
#         cpf = request.POST.get('cpf')
#         codigo_pulseira = request.POST.get('id_pulseira')

#         try:
#             ingresso = Ingresso.objects.get(cpf=cpf, codigo_pulseira=codigo_pulseira, status_pagamento='pago')
#             request.session['usuario_id'] = ingresso.id  # ESSENCIAL
#             print(request.session.get('usuario_id'))
#         except Ingresso.DoesNotExist:
#             return render(request, 'frontend/registrar.html', {
#                 'erro': 'Dados não encontrados ou pagamento não confirmado.'
#             })

#         return render(request, 'frontend/registrar.html', {
#             'sucesso': 'Registro confirmado! Você pode acessar os recursos do festival.'
#         })
    







