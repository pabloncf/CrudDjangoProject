from rest_framework import serializers
from .models import Carro,Cliente

class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = ['id','nome','modelo','preco','placa']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id','nome','endereco','telefone','id_carro_alugado']