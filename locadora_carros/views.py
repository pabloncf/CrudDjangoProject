from django.shortcuts import render
from rest_framework import viewsets
from .models import Carro,Cliente
from .serializer import CarroSerializer,ClienteSerializer
from django.core.paginator import Paginator

# Create your views here.

class CarroViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all().order_by('id')
    serializer_class = CarroSerializer
    carro_paginator = Paginator(queryset,20)

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('nome')
    serializer_class = ClienteSerializer
    cliente_paginator = Paginator(queryset,20)