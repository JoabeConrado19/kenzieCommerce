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