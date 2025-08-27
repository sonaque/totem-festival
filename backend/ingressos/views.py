from django.shortcuts import render

# Create your views here.

def ingressos1(request):
    return render(request,'frontend/ingressos1.html')

def cadastro(request):
    return render(request,'frontend/cadastro.html')


