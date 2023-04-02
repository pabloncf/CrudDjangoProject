# CRUD para uma locadora de carros

## Funcionamento

    * Terá como cadastrar clientes e carros que a locadora possui
    * A locadora irá cadastrar o cliente e o sistema irá gerar um id para esse cliente
    * No cadastro,irá ter o campo para ligar o cliente ao carro que foi alugado por ele.

## Funcionamento do codigo

    Pasta /locadora_carros
        * Primeiro foi feito o models.py, onde foi inserido no banco os clientes e os carros que serão cadastrados, criando uma tabela com limitações e parâmetros especificos para cada coluna.
        
        * Depois foi feito a parte do admin.py para adminstração do banco pelo painel admin da aplicação, que pode ser acessado com: http://localhost:8000/admin (Claro, no caso utilizando isso em uma máquina local. No caso da aplicação estar alocada em um servidor, será: http://dominiodoseusite.com/admin)

        * Depos fomos para o serializer.py, que serve basicamente para tradução e tratamento dos dados vindos do banco para o formato JSON.

        * Após isso fomos para o views.py, onde fizemos a impressão para o usuário utilizando o django rest framework.
    Pasta /setup
        * Por fim, modificamos o arquivo de urls para que assim que o cliente entre na parte principal da página, ele escolha se quer adicionar um cliente ou um carro
## Observações do codigo
    * Foi feita relacionamento com entidades no arquivo models.py, fazendo a ligação do id do carro com o carro que o cliente alugou:

    ```
    class Carro(models.Model):
        id = models.UUIDField(primary_key=True,default=uuid4,editable=False)

    class Cliente(models.Model):
        id_carro_alugado = models.ForeignKey(Carro, on_delete=models.CASCADE)
    ```

    * Também foi feito a paginação no arquivo views.py, para limitação de 20 objetos por página:
    ```
    from django.core.paginator import Paginator
        class CarroViewSet(viewsets.ModelViewSet):
            queryset = Carro.objects.all().order_by('id')
            serializer_class = CarroSerializer
            carro_paginator = Paginator(queryset,20)

        class ClienteViewSet(viewsets.ModelViewSet):
            queryset = Cliente.objects.all().order_by('nome')
            serializer_class = ClienteSerializer
            cliente_paginator = Paginator(queryset,20)
    ```

    * Foi adicionado a biblioteca do uuid para criação de ids para a primary_keys da tabela de carros
## Observações do projeto

    * Para o cliente poder modificar ou/e deletar ele terá que colocar após a url um /o_que_quer_modificar/id
    Exempo: http://localhost:8000/carros/854248923

    * Neste projeto não foi feito nada do front-end. Tudo foi com django rest framework


### Made by Pablo Cunha