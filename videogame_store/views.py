from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Jogo,Loja
from .serializer import JogoSerializer,LojaSerializer
# Create your views here.

class JogoViewSet(viewsets.ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer

class LojaViewSet(viewsets.ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer
