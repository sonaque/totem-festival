# from django.db import models

# class Ingresso(models.Model):
#     nome_cliente = models.CharField(max_length=100)
#     tipo_ingresso = models.CharField(max_length=50)
#     valor = models.DecimalField(max_digits=8, decimal_places=2)
#     status_pagamento = models.CharField(max_length=20, default='pendente')  # pendente, aprovado
#     codigo_qr = models.CharField(max_length=255, blank=True, null=True)
#     criado_em = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.nome_cliente} - {self.tipo_ingresso} - {self.status_pagamento}"
