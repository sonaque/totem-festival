from django.shortcuts import render, redirect
from ingressos.models import Ingresso

def registrar_pulseira(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf')
        codigo_pulseira = request.POST.get('id_pulseira')

        try:
            ingresso = Ingresso.objects.get(cpf=cpf, codigo_pulseira=codigo_pulseira, status_pagamento='pago')
            request.session['usuario_id'] = ingresso.id 
            return redirect('pagina_principal') 
        except Ingresso.DoesNotExist:
            return render(request, 'frontend/registrar.html', {
                'erro': 'Dados não encontrados ou pagamento não confirmado.'
            })

    return render(request, 'frontend/registrar.html')


