from django.shortcuts import render
from rest_framework import viewsets
from .models import Carro,Cliente
from .serializer import CarroSerializer,ClienteSerializer

# Create your views here.

class CarroViewSet(viewsets.ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer