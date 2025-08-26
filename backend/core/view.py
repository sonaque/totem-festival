from django.shortcuts import render

def mapa(request):
    return render(request, 'frontend/mapa.html')

def pagina_principal(request):
    return render(request, 'frontend/pagina_principal.html')

def programacao(request):
    return render(request, 'frontend/programacao.html')

def bar(request):
    return render(request, 'frontend/bar.html')



    