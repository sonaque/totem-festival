from django.shortcuts import render, redirect
from .models import Usuario
import uuid
from datetime import datetime

def mostrar_registro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        tipo_ingresso = request.POST.get('tipo_ingresso')

        pulseira_id = str(uuid.uuid4())  # Gera ID único
        pagamento_confirmado = True  # ou False, dependendo da lógica

        Usuario.objects.create(
            nome=nome,
            cpf=cpf,
            email=email,
            tipo_ingresso=tipo_ingresso,
            pulseira_id=pulseira_id,
            pagamento_confirmado=pagamento_confirmado,
            data_chegada = datetime.now.time()
        )

        return redirect('registro_sucesso')  # ou renderizar uma página de confirmação

    return render(request, 'frontend/registro.html')
