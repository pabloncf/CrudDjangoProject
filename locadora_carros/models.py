from django.db import models
from uuid import uuid4

# Create your models here.

class Carro(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    nome = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    placa = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    id_carro_alugado = models.CharField(max_length=100)

    def __str__(self):
        return self.nome