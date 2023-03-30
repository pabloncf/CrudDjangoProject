from django.contrib import admin
from .models import Jogo, Loja,Clientes

# Register your models here.

class JogosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco') #serve para imprimir na tela os parametros especificados

admin.site.register(Jogo, JogosAdmin) #serve para enviar

class LojaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone')

admin.site.register(Loja, LojaAdmin)

class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone')

admin.site.register(Clientes, ClientesAdmin)