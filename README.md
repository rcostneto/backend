# Minha API

Este projeto foi pensado em atender a demanda de uma *Oficina_de_Peças* **VS Motos**

Essa API(backend) irá fornecer a empresa contratante o inclusão, exclusão e visualização do produto, fornecedor e usuários(atualização).
Logo abaixo informa como executar a API.

---
## Como executar 


Após efetuar o download do repositório e com o VSCode aberto, abra a pasta Gerenciamento peças oficina, clicando em Arquivo/Abrir Pasta.
Em seguida clique com o botao direio do mouse em backend e com o esquerdo Abrir no Terminal Integrado.

> Não é obrigatório mas será recomendado usar o virtualenv, uma vez que o projeto foi elaborado com essa ferramenta.
 [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

Digite o comando abaixo no terminal para instalar o virtualenv
```
python3 -m venv env
```

Com o env instalado agora iremos ativá-lo.
```
./env/Scripts/activate
```

agora iremos instalar todas as libs/bibliotecas python listadas no `requirements.txt` instaladas.
```
(env)$ pip install -r requirements.txt
```
>*Após instalar as libs é recomendado que faça uma atualização do comando* `pip`
>>python.exe -m pip install --upgrade pip


Para executar a API(backend)  basta executar o comando abaixo.
```
(env)$ flask run --host 0.0.0.0 --port 5000
```

 Caso esteja desenvolvendo e precise atualizar o código fonte, será necessário usar o comando acima com --reload descrito no comando abaixo.
```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

---
### *Como usar*

>OBS
Logo após a execução da API, uma página com a documentação será aberta em Swagger, Redoc ou RapiDoc, nesse exemplo falaremos da Swagger que servirá para a restante, pois o propósito delas são o mesmo, outro fato é a respeito das rotas, foi implementado 15 rotas, porém como requisito do MVP foi sugerido pelo menos 3 rotas e 1 como POST para cadastro, dessa forma trataremos de 5 rotas(POST/usuario, POST/update_usuario, GET/usuario, GET/usuarios, DELETE/usuario) referentes a uma tabela de usuário.
---

#### **POST/usuario**

Com o Swagger aberto iremos a procura da rota POST /usuario para efetuar o cadastro de usuarios na tabela.
```
Clique em Adicionar um novo usuario a base de dados, em seguida em "Try it out" para liberar os campos a serem preenchidos.
preencha os campos(cpf, data_nascimento, email, login, nome, senha, senha_novamente, sobrenome) e clique em execute.
```

>Obs: Note que os campos possuem restrições e que devera ser preenchido assim como mostra os valores default. No caso de login minimo de 4 caracteres e no máximo 10 caracteres, enquanto a senha o máximo é 10 caracteres.

>Cod:200 - indica que o cadastro foi realizado com sucesso.
>Cod:409 - indica que os dados ja constam no banco.
>Cod:400 - indica que algum dado não foi preenchido corretamente.

---

#### **GET/usuario**

```
Clique em Faz a busca por um Usuario a partir de seu nome, em seguida em "Try it out" para liberar os campos a serem preenchidos.
preencha o campo nome e clique em execute.
```

>Obs: Nesse caso a busca sera feita pelo nome do usuario, o codigo abaixo indica o status da busca.

>Cod:200 - Usuario econtrado.
>Cod:404 - Usuario não encontrado na base.

---

#### **GET/usuarios**

```
Clique em Faz a busca por todos os Usuario cadastrados na base de dados, em seguida em "Try it out" para liberar os campos a serem preenchidos.
clique em execute.
```

>Obs: Nesse caso a busca ira trazer uma lista de todos os usuarios no banco, caso na haja nenhum, a lista retornara vazia.

>Cod:200 - Usuarios econtrados.
>Cod:200 - [].

---

#### **DELETE/usuario**

```
Clique em Deleta um Usuario a partir do nome informado, em seguida em "Try it out" para liberar os campos a serem preenchidos.
clique em execute.
```

>Obs: Deleta um usuario a partir de seu nome.

>Cod:200 Usuario removido.
>Cod:404 Usuario não encontrado no banco.







