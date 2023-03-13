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

<h2 align="center">Endpoints</h2>

