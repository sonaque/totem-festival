from django.shortcuts import render, redirect
from ingressos.models import Ingresso

def registrar_pulseira(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        codigo_pulseira = request.POST.get('id_pulseira')

        try:
            ingresso = Ingresso.objects.get(cpf=cpf, codigo_pulseira=codigo_pulseira, status_pagamento='pago')
            request.session['usuario_id'] = ingresso.id  # SALVA NA SESSÃO
            return redirect('pagina_principal')  # Redireciona para o bar
        except Ingresso.DoesNotExist:
            return render(request, 'frontend/registrar.html', {
                'erro': 'Dados não encontrados ou pagamento não confirmado.'
            })

    # Requisição GET: só exibe o formulário
    return render(request, 'frontend/registrar.html')


