from django.db import models

class Usuario(models.Model):
    TIPO_INGRESSO_CHOICES = [
        ('pista', 'Pista'),
        ('camarote', 'Camarote'),
    ]

    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    pulseira_id = models.CharField(max_length=100, unique=True)
    tipo_ingresso = models.CharField(max_length=10, choices=TIPO_INGRESSO_CHOICES)
    pagamento_confirmado = models.BooleanField(default=False)
    data_chegada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.tipo_ingresso})"
