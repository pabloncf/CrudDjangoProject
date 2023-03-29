#arquivo para traduzir de python para json
from rest_framework import serializers
from .models import Jogo,Loja

class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo    #nome do modulo que será processado
        fields = ['nome','preco']   #campos que serão processados
    
class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = ['nome','endereco','telefone']