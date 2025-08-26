from django.db import models
from ingressos.models import Ingresso

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.IntegerField(help_text="Preço em centavos")
    imagem = models.CharField(max_length= 200)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    usuario = models.ForeignKey(Ingresso, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    id_cobranca = models.CharField(max_length=100, unique=True)
    status_pagamento = models.CharField(max_length=20, default='pendente')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.nome_cliente} comprou {self.produto.nome} - {self.status_pagamento}"