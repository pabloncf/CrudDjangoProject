from django.contrib import admin
from .models import Carro,Cliente

# Register your models here.

class CarroAdmin(admin.ModelAdmin):
    list_display = ('id','nome','modelo','preco')

admin.site.register(Carro, CarroAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id','nome','endereco','telefone','id_carro_alugado')

admin.site.register(Cliente,ClienteAdmin)