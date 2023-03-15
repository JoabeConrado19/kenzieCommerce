<h1 align="center">KenzieCommerceAPI</h1>

<blockquote>
    <br>
        <p>Este é um projeto de API construinda em python para suportar uma plataforma de e-commerce com diferentes níveis de acesso.</p>
        <p>O objetivo principal é permitir que os usuários possam buscar, comprar e vender produtos na plataforma.</p>
    <br>
</blockquote>
<br>
     <h3>Tecnlogias usadas </h3>
<hr>
<blockquote>
     <br>
        <ul>
            <li>Python (linguagem principal)</li>
            <li>Django (Framework)</li>
            <li>Django Rest Framework (biblioteca utilizada para construção da APIRest)</li>
            <li>python-dotenv (gerenciamento de variaveis de ambiente)</li>
            <li>PostgreSQL (ferramenta de banco de dados relacionais)</li> 
            <li>pip (gerenciamento de pacotes python)</li>
            <li>git (controle de versionamento)</li>
            <li>IPDB (biblioteca para debug)</li>
        </ul>
     <br>
</blockquote>
<br>
<h2 align="center">Funcionalidades e níveis de acesso</h2>
<hr>
<br>
<h3>1. Usuários</h3>
    <blockquote>
        <br>
            <p>A api permite o cadastro de usuários, existem três tipos usuários:</p>
                <ul>
                    <li>Administrador,</li>
                    <li>Vendedor,</li>
                    <li>Cliente,</li>
                </ul>    
            <br>
            <p>Usuários não autenticados podem acessar a plataforma para visualizar informações sobre os produtos.</p>
        <br>
    </blockquote>
<br>
<h3>1.1 Níveis de acesso</h3>
<br>
    <blockquote>
        <br>
            <ul>
                <li><b>Administrador:</b>     Tem acesso a todas as rotas e pode transformar um usuário comum em vendedor.</li>
                <br>
                <li><b>Vendedor:</b> Pode cadastrar novos produtos na plataforma, atualizar estoque de determinado produto, verificar os pedidos realizado dos produtos cadastrado por ele e também tem acesso a todas as rotas de um cliente</li>
                <br>
                <li><b>Cliente:</b> Pode atualizar o perfil para se tornar vendedor, adicionar produtos ao carrinho e finalizar a compra dos produtos. Também tem uma rota para visualizar todos os pedidos comprados.</li>
            </ul>
        <br>
    </blockquote>
<br>
<h3>2. Endereço</h3>
    <blockquote>
        <br>
            <p>O usuário tem a possibilidade de criar um endereço.</p>
        <br>
    </blockquote>
<br>
<h3>3. Produtos</h3>
    <blockquote>
        <br>
            <ul>
                <li>O usuário pode buscar os produtos por nome, categoria e id.</li>
                <li>Tem verificação de estoque do itens, com indicação de indisponibilidade quando o item estiver com 0 unidades.</li>
                <li>Quando um pedido é criado, a quantidade de estoque é subtraído.</li>
                <li>Caso um usuário tenha um produto no carrinho e este produto esteja indisponível ao finalizar a compra, retornar um erro indicando que o produto não está mais disponível.</li>
            </ul>
        <br>
    </blockquote>
<br>
<h3>4. Carrinho de Compra</h3>
    <blockquote>
        <br>
            <ul>
                <li>Os produtos selecionados pelo usuário são armazenados no carrinho antes de finalizar a compra.</li>
                <li>No carrinho, contém uma lista dos produtos selecionados com os valores dos items</li>
                <li>O pedido não é finalizado, caso o produto não tenha estoque ou caso ele esteja indisponivel.
                <li>Se os produtos do carrinho forem de diferentes vendedores, é criado um pedido diferente para cada.</li>
            </ul>
        <br>
    </blockquote>
<br>
<h3>5. Pedido</h3>
    <blockquote>
        <br>
            <ul>
                <li>Os pedidos tem um status de PEDIDO REALIZADO, EM ANDAMENTO ou ENTREGUE para acompanhamento do usuário.</li>
                <li>Toda vez que o status do pedido for atualizado, é enviado um email ao vendedor.</li>
                <li>O vendedor do produto conseguer atualizar o status do pedido.</li>
                <li>Contém o horário em que o pedido foi feito</li>
            </ul>
        <br>
    </blockquote>
<br>
<h2 align="center">Instalação e configuração</h2>
<hr>
<br>
<blockquote>
    <br>
        <p align="center">Para rodar a aplicação, é necessário ter o Python 3.7 ou superior instalado. Também é necessário instalar as dependências listadas no arquivo requirements.txt</p>
    <br>
</blockquote>
<br>
<br>
    <p>Para instalar as dependencias necessarias para rodar a API, siga os passos abaixo:</p>
<br>
    <p>1 - Clone este repositório em seu computador:</p>
    <p>2 - Crie um ambiente virtual para instalar as dependencias do projeto.</p>
<br>
    <span>No terminal digite o comando abaixo para criar seu ambiente virtual</span>


~~~bash
python -m venv venv
~~~
<br>
    <p>3 - Com o ambiente virtual criado, é hora de instalar as dependencias do projeto</p>
    <span>No terminal digite o comando abaixo para instalar as dependencias</span>

~~~bash
pip install -r requirements.txt
~~~

<p>4 - Crie um arquivo .env com as mesmas variaveis do arquivo .env.example para realizar as configurações do banco de dados </p>
<blockquote>
    <br>
        <p align="center">ATENÇÃO</p>
        <p align="center">Os nomes das variavies precisam ser iguais aos exemplos do arquivo .env.example</p>
    <br>
</blockquote>

<br>
<p>5 - Para criar as tabelas no banco de dados, rode o seguinte comando no terminal:</p>

~~~bash
python manage.py migrate
~~~

<br>
<p>6 - Para iniciar a aplicação, execute o seguinte comando no terminal e o api estará rodando:</p>

~~~bash
python manage.py runserver
~~~
<br>
<h2 align="center">Endpoints</h2>
<br>
<hr>
<br>

###

<details> 
    <summary>Rotas sem autorização</summary>
<br>
    <h3> 1. Listar todos os usuarios</h3>

```http
GET http://127.0.0.1:8000/api/users/
```
<details>
    <summary>Listar</summary>

```json
    STATUS_CODE/ 200 OK
    {
        "count": 4,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 1,
                "first_name": "thiago",
                "last_name": "silva",
                "email": "thiago@mail.com",
                "cpf": "15940806",
                "is_superuser": false,
                "is_seller": false,
                "username": "thiago"
            },
            {
                "id": 2,
                "first_name": "admin",
                "last_name": "admin",
                "email": "admin@mail.com",
                "cpf": "15940803",
                "is_superuser": true,
                "is_seller": true,
                "username": "admin"
            }
        ]
}
```
</details>



<br>
<h3>Criar os usuarios</h3>

```http
POST http://127.0.0.1:8000/api/users/
```
<details> 
    <summary>Campos Obrigatórios</summary>

```json
    STATUS_CODE 400 BAD_REQUEST
        {
        "first_name": [
            "This field is required."
        ],
        "last_name": [
            "This field is required."
        ],
        "email": [
            "This field is required."
        ],
        "password": [
            "This field is required."
        ],
        "cpf": [
            "This field is required."
        ]
    }
```

</details>

<details>
    <summary>Criação de usuario comum</summary>

```json
    Exemplo de body request
    {
        "first_name": "Thiago R",
        "last_name": "Silva",
        "email": "trs@mail.com",
        "password": "tes124@303",
        "cpf": "12345678",
        "username": "Thiao R"
    }
```

```json
    Resposta esperada request
    STATUS_CODE 201 CREATED
    {
        "id": 1,
        "first_name": "Thiago R",
        "last_name": "Silva",
        "email": "trs@mail.com",
        "cpf": "12345678",
        "is_superuser": false,
        "is_seller": false,
        "username": "Thiao R"
    }
```
</details>



<details>
    <summary>Criação de Vendedor</summary>
    
```json
    Exemplo de body request
    {
        "first_name": "Chiquinho",
        "last_name": "Mendoça",
        "email": "chico@mail.com",
        "password": "tes124@303",
        "cpf": "12345679",
        "username": "chico",
        "is_seller": true
    }
```
```json
    Resposta esperada 
    STATUS_CODE 201 CREATED
    {
        "id": 2,
        "first_name": "Chiquinho",
        "last_name": "Mendoça",
        "email": "chico@mail.com",
        "cpf": "12345679",
        "is_superuser": false,
        "is_seller": true,
        "username": "chico"
    }
```
</details>

<details>
    <summary>Criação de Admin</summary>

```json
    Exemplo de body request
    {
        "first_name": "Admin",
        "last_name": "Admin",
        "email": "admin@mail.com",
        "password": "tes124@303",
        "cpf": "12345789",
        "username": "admin",
        "is_seller": true,
        "is_superuser":true
    }
```
```json
    Resposta esperada 
    STATUS_CODE 201 CREATED
    
    {
        "id": 3,
        "first_name": "Admin",
        "last_name": "Admin",
        "email": "admin@mail.com",
        "cpf": "12345789",
        "is_superuser": true,
        "is_seller": true,
        "username": "admin"
    }
    
```

</details>
<br>
<h3>3. Login</h3>


```http
POST http://127.0.0.1:8000/api/users/login/
```

<details>
    <summary>Fazer Login</summary>

```json
    Exemplo de body request
    {
	"email": "trs@mail.com",
	"password": "tes124@303"
    }
```

```json
    Resposta esperada 
    STATUS_CODE 200 OK
    
{
	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3OTQwNTM0NiwiaWF0IjoxNjc4ODAwNTQ2LCJqdGkiOiI2MWViNWEwNGY2ZDI0YTk4YTFlMDNlMjA0YmZlZTA3NSIsInVzZXJfaWQiOjZ9.4QFEgnwyHWjunQGpPerdQZZjcclcZ9Z24nnH8qYNCkY",
	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc4ODI5MzQ2LCJpYXQiOjE2Nzg4MDA1NDYsImp0aSI6IjY1Y2E0NGM3OTU0NjQzYTdhM2U1OWU2NmVkZWI4YTk4IiwidXNlcl9pZCI6Nn0.fyyqNrcH15LG2pZxQxwU5PYZ-eoqDWfncqpUzUs8jgE"
}
    
```
</details>
<br>
<br>
<h3>4.Produtos</h3>

```http
GET http://127.0.0.1:8000/api/products/
```

<details>
    <summary>Listar todos os produtos</summary>

```json
    STATUS CODE 200 0k

    {
	"count": 10,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": 1,
			"name": "webcam",
			"category": "eletronico",
			"description": null,
			"price": 1.0,
			"stock": 3,
			"available": false,
			"seller": {
                "id": 2,
                "first_name": "Chiquinho",
                "last_name": "Mendoça",
                "email": "chico@mail.com",
                "cpf": "12345679",
                "is_superuser": false,
                "is_seller": true,
                "username": "chico"
            },
			"img": null
		},
		{
			"id": 2,
			"name": "webcam Furada",
			"category": "eletronico",
			"description": null,
			"price": 1.0,
			"stock": 0,
			"available": true,
			"seller": {
                "id": 2,
                "first_name": "Chiquinho",
                "last_name": "Mendoça",
                "email": "chico@mail.com",
                "cpf": "12345679",
                "is_superuser": false,
                "is_seller": true,
                "username": "chico"
            },
			"img": null
		},
		{
			"id": 3,
			"name": "teclado",
			"category": "eletronico",
			"description": null,
			"price": 1.0,
			"stock": -3,
			"available": false,
			"seller": {
                "id": 2,
                "first_name": "Chiquinho",
                "last_name": "Mendoça",
                "email": "chico@mail.com",
                "cpf": "12345679",
                "is_superuser": false,
                "is_seller": true,
                "username": "chico"
            },
			"img": null
		},
    ]
```

</details>

</details>
<br>
<hr>
<br>

###

<details>
    <summary>Rotas com autenticação</summary>
<br>
<blockquote>
    <br>
    <p align="center">O Admin tem acesso a todos as rotas</p>
    <br>
</blockquote>
<br>

<h3>1. Atualizar Usuario e deletar </h3>

```http
PATCH http://127.0.0.1:8000/api/users/id/
Authorization: Bearer token
```
<p>Deve passar o id do usuario quer será feito o update</p>
<p>Somente Admin ou o próprio usuario consegue fazer a atualização</p>
<details>
    <summary>Update</summary>
    
```json
    Exemplo de body request
    {
	"is_seller": true
    }
```

```json
   STATUS CODE 200 0k
    {
        "id": 1,
        "first_name": "thiago",
        "last_name": "silva",
        "email": "thiago@mail.com",
        "cpf": "15940806",
        "is_superuser": false,
        "is_seller": true,
        "username": "thiago"
    }
```


</details>
<details>
    <summary>Delete</summary>   
<br>
<p>só passar o ID do usuario que será deletado no fim do endpoint</p>
<br>
<p>Resposta esperada:</p>

```json
    STATUS CODE 204 No Content
```
</details>
<br>
<br>
<h3>2. Criar Produto </h3>

```http
POST http://127.0.0.1:8000/api/products/
Authorization: Bearer token
```
<br>
<details>
    <summary>Criação</summary>

```json
    Exemplo de body request
    {
        "name":"Playstation 5",
        "category": "eletronicos",
        "price": 4000,
        "stock": 30,
        "description": "Desfrute do carregamento do seu PS5, extremamente rápido com o SSD de altíssima velocidade, uma imersão mais profunda com suporte a feedback tátil, gatilhos adaptáveis e áudio 3D, além de uma geração inédita de jogos incríveis para PlayStation.",
        "img": "https://images.kabum.com.br/produtos/fotos/238671/console-sony-playstation-5_1634132554_m.jpg"
    }
```

```json
    Resposta esperada 
    STATUS_CODE 201 Created
    
{
	"id": 1,
	"name": "Playstation 5",
	"category": "eletronicos",
	"description": "Desfrute do carregamento do seu PS5, extremamente rápido com o SSD de altíssima velocidade, uma imersão mais profunda com suporte a feedback tátil, gatilhos adaptáveis e áudio 3D, além de uma geração inédita de jogos incríveis para PlayStation.",
	"price": 4000.0,
	"stock": 30,
	"available": true,
	"seller":   {
        "id": 2,
        "first_name": "thiago",
        "last_name": "silva",
        "email": "thiago@mail.com",
        "cpf": "15940806",
        "is_superuser": false,
        "is_seller": true,
        "username": "thiago"
    },
	"img": "https://images.kabum.com.br/produtos/fotos/238671/console-sony-playstation-5_1634132554_m.jpg"
}
    
```

</details>
<br>
<h3>3. Carrinho de compra </h3>
<br>

```http
http://127.0.0.1:8000/api/shopping/
Authorization: Bearer token
```
<details>
<summary>Alocar produto ao carrinho</summary>
<br>
<blockquote>
<br>
    <p>Para alocar um produto ao carrinho só passar no final do endpoint o ID do produto, que ele será alocado a uma lista do usuario logado, conforme exemplo abaixo:</p>
<br>

```http
POST http://127.0.0.1:8000/api/shopping/1/
Authorization: Bearer token
```

```json
    Resposta esperada 
    STATUS_CODE 201 Created
    
{
	"id": 1,
	"user": 1,
	"items": [
		{
			"id": 1,
			"product": {
				"id": 1,
				"name": "Playstation 5",
				"category": "eletronicos",
				"description": "Desfrute do carregamento do seu PS5, extremamente rápido com o SSD de altíssima velocidade, uma imersão mais profunda com suporte a feedback tátil, gatilhos adaptáveis e áudio 3D, além de uma geração inédita de jogos incríveis para PlayStation.",
				"price": 4000.0,
				"stock": 30,
				"available": true,
				"seller":{
                    "id": 2,
                    "first_name": "Chiquinho",
                    "last_name": "Mendoça",
                    "email": "chico@mail.com",
                    "cpf": "12345679",
                    "is_superuser": false,
                    "is_seller": true,
                    "username": "chico"
                },
				"img": "https://images.kabum.com.br/produtos/fotos/238671/console-sony-playstation-5_1634132554_m.jpg"
			},
			"quantity": 1
		}
	]
}
    
```
<br>
<hr>
    <p align="center">É possivel também passar uma quantidade do produto atráves do endpoint, conforme exemplo abaixo:</p>
<br>

```http
POST http://127.0.0.1:8000/api/shopping/1/?quantity=10
Authorization: Bearer token
```

```json
    Resposta esperada 
    STATUS_CODE 201 Created
    
{
	"id": 1,
	"user": 1,
	"items": [
		{
			"id": 1,
			"product": {
				"id": 1,
				"name": "Playstation 5",
				"category": "eletronicos",
				"description": "Desfrute do carregamento do seu PS5, extremamente rápido com o SSD de altíssima velocidade, uma imersão mais profunda com suporte a feedback tátil, gatilhos adaptáveis e áudio 3D, além de uma geração inédita de jogos incríveis para PlayStation.",
				"price": 4000.0,
				"stock": 30,
				"available": true,
				"seller":{
                    "id": 2,
                    "first_name": "Chiquinho",
                    "last_name": "Mendoça",
                    "email": "chico@mail.com",
                    "cpf": "12345679",
                    "is_superuser": false,
                    "is_seller": true,
                    "username": "chico"
                },
				"img": "https://images.kabum.com.br/produtos/fotos/238671/console-sony-playstation-5_1634132554_m.jpg"
			},
			"quantity": 10
		}
	]
}
    
```
<br>
</blockquote>
</details>

<details>
    <summary>Lista de produtos do carrinhos</summary>
    <blockquote>
        <br>
            <p>Só realizer um get no endpoint do carrinho, que ele irá retornar todos os produtos selecionados pelo usuario, caso não haja nenhum produto listado, uma lista vazia será retornado.</p>
        <br>
    </blockquote>

```http
GET http://127.0.0.1:8000/api/shopping/
Authorization: Bearer token
```
```json
    Resposta esperada 
    STATUS_CODE 200 Ok
    
{
	"id": 1,
	"user": 1,
	"items": [
		{
			"id": 1,
			"product": {
				"id": 1,
				"name": "Playstation 5",
				"category": "eletronicos",
				"description": "Desfrute do carregamento do seu PS5, extremamente rápido com o SSD de altíssima velocidade, uma imersão mais profunda com suporte a feedback tátil, gatilhos adaptáveis e áudio 3D, além de uma geração inédita de jogos incríveis para PlayStation.",
				"price": 4000.0,
				"stock": 30,
				"available": true,
				"seller":{
                    "id": 2,
                    "first_name": "Chiquinho",
                    "last_name": "Mendoça",
                    "email": "chico@mail.com",
                    "cpf": "12345679",
                    "is_superuser": false,
                    "is_seller": true,
                    "username": "chico"
                },
				"img": "https://images.kabum.com.br/produtos/fotos/238671/console-sony-playstation-5_1634132554_m.jpg"
			},
			"quantity": 1
		}
	]
}
    
```
</details>

<details>
    <summary>Deletar produtos do carrinho</summary>

```http
DELETE http://127.0.0.1:8000/api/shopping/
Authorization: Bearer token
```
<br>
<br>
    <p>Todos os produtos do carrinho serão deletados</p>
    <p>Retorno esperado:</p>

```json
    STATUS CODE 204 No Content
```
</details>
<br>
<h3>4. Pedido </h3>
<details>
    <summary>Criação do pedido</summary>
    <blockquote>
        <br>
            <p>Usuario precisa estar logado e só fazer um POST no endpoint da ORDER que o pedido será criado, ele irá pegar a lista de produtos do carrinho e alocar no pedido</p>
        <br>
    </blockquote>
    
```http
POST http://127.0.0.1:8000/api/order/
Authorization: Bearer token
```

```json
    Resposta esperada 
    STATUS_CODE 200 Ok
    
{
	"message": "Pedidos criados com sucesso"
}
    
```

</details>

<details>
    <summary>Confirmar pedido</summary>
    <blockquote>
        <br>
             <p>O usuário vendedor precisa estar logado e passar o ID no final do endpoint, caso no body da requisição ele passe o confirmed_order como true a ORDER será confirmada e o status do pedido passará para "Em Andamento", caso seja passado false o pedido será recusado e será deletado.</p>
        <br>
    </blockquote>
    
```http
PATCH http://127.0.0.1:8000/api/order/1/
Authorization: Bearer token
```

```json
    body
    {
	"confirmed_order": true
    }
```


```json
    Resposta esperada 
    STATUS_CODE 200 Ok
    
{
	"message": "Pedido em andamento"
}
    
```
<br>
<br>
<blockquote>
        <br>
            <p>Para o usuário cliente será utilizada a mesma rota. Caso o pedido não esteja confirmado pelo vendedor aparecerá um erro para o cliente, caso o pedido já esteja confirmado e seja passado o confirmed_order como true o status do pedido será alterado para "Entregue"</p>
        <br>
</blockquote>

```json
    body
    {
	    "confirmed_order": true
    }
```


```json
    Resposta esperada 
    STATUS_CODE 200 Ok
    
    {
	    "message": "Pedido entregue"
    }
    
```
</details>

<details>
    <summary>Listar Pedidos</summary>
    <blockquote>
        <br>
            <p>Rota de acesso do vendedor, todos os pedidos dos produtos vendidos pelo vendedor logado será retornado como uma lista</p>
        <br>
    </blockquote>
<br>

```http
    GET http://127.0.0.1:8000/api/order/
    Authorization: Bearer token
```
```json
    Resposta esperada 
    STATUS_CODE 200 Ok
    [
        {
            "id": 1,
            "ordered_products": [
                {
                    "id": 12,
                    "name": "Playstation 5",
                    "category": "eletronicos",
                    "price": 4000.0,
                    "quantity": 1,
                    "buyer": 2,
                    "order": 34,
                    "product": 11
                }
            ],
            "status": "Entregue",
            "buyed_at": "2023-03-14T14:56:02.729576Z",
            "totalPrice": "4000.00",
            "totalQuantity": 1,
            "user": 2
        },
        {
            "id": 2,
            "ordered_products": [
                {
                    "id": 13,
                    "name": "Playstation 5",
                    "category": "eletronicos",
                    "price": 4000.0,
                    "quantity": 10,
                    "buyer": 4,
                    "order": 38,
                    "product": 11
                }
            ],
            "status": "pedido_realizado",
            "buyed_at": "2023-03-14T16:03:21.699708Z",
            "totalPrice": "40000.00",
            "totalQuantity": 2,
            "user": 2
        },
        {
            "id": 3,
            "ordered_products": [
                {
                    "id": 14,
                    "name": "Playstation 5",
                    "category": "eletronicos",
                    "price": 4000.0,
                    "quantity": 10,
                    "buyer": 1,
                    "order": 42,
                    "product": 11
                }
            ],
            "status": "pedido_em_andamento",
            "buyed_at": "2023-03-14T16:11:51.492573Z",
            "totalPrice": "40000.00",
            "totalQuantity": 10,
            "user": 2
        }
    ]
```

</details>

</details>
<br>
<hr>
<br>

<h2 align="center"> Acessar a documentação completa </h2>


<p>Para visualizar todos os endpoints da aplicação, só acessar o link abaixo: </p>

    https://kenziecommerce-production.up.railway.app/api/docs/swagger-ui/











