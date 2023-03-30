from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Jogo,Loja,Clientes
from .serializer import JogoSerializer,LojaSerializer,ClientesSerializer
# Create your views here.

class JogoViewSet(viewsets.ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer

class LojaViewSet(viewsets.ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializer
