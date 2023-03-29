from django.db import models

# Create your models here.

class Jogo(models.Model):
    nome = models.CharField(max_length=100) #definindo a que a variável nome pode ter apenas 100 caracteres e que será uma string
    preco = models.DecimalField(max_digits=7,decimal_places=2) #definindo que a variavel preco terá no máximo 7 digitos e 2 casas decimais

    def __str__(self):
        return self.nome

class Loja(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)

    def __str__(self):
        return self.nome