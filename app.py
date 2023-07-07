from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import Session, Usuario
from logger import logger
from schemas import *
from flask_cors import CORS

info = Info(title="VS Motos", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
usuario_tag = Tag(name="Usuario", description="Adicao, visualizacao e remoção de usuarios a base de dados")


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


@app.post('/usuario', tags=[usuario_tag],
          responses={"200": UsuarioViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_usuario(form: UsuarioSchema):
    """Adiciona um novo Usuario à base de dados

    Retorna uma representação dos usuarios.
    """
    usuario = Usuario(
        nome = form.nome,
        sobrenome = form.sobrenome,
        cpf = form.cpf,
        data_nascimento = form.data_nascimento,
        email = form.email,
        login = form.login,
        senha = form.senha,
        senha_novamente = form.senha_novamente)
    logger.debug(f"Adicionando usuario de nome: '{usuario.nome}'")
    try:
        # criando conexão com o banco
        session = Session()
        # adicionando usuario
        session.add(usuario)
        # efetivando o comando de adição de novo usuario na tabela
        session.commit()
        logger.debug(f"Adicionado usuario de nome: '{usuario.nome}'")
        return apresenta_usuario(usuario), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Esse usuário ja existe no banco :/"
        logger.warning(f"Erro ao adicionar usuario '{usuario.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "O usuário não foi salvo no banco :/"
        logger.warning(f"Erro ao adicionar usuario '{usuario.nome}', {error_msg}")
        return {"mesage": error_msg}, 400
    

@app.delete('/usuario', tags=[usuario_tag],
            responses={"200": UsuarioDelSchema, "404": ErrorSchema})
def del_usuario(query: UsuarioBuscaSchema):
    """Deleta um Usuario a partir do nome informado

    Retorna uma mensagem de confirmação da remoção.
    """
    usuario_nome = unquote(unquote(query.nome))
    print(usuario_nome)
    logger.debug(f"Deletando dados sobre usuario #{usuario_nome}")
    # criando conexão com o banco
    session = Session()
    # fazendo a remoção
    count = session.query(Usuario).filter(Usuario.nome == usuario_nome).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado usuario #{usuario_nome}")
        return {"mesage": "Usuario foi removido", "id": usuario_nome}
    else:
        # se o fornecedor não foi encontrado
        error_msg = "Usuario não foi encontrado no banco :/"
        logger.warning(f"Erro ao deletar o usuario #'{usuario_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    

@app.get('/usuario', tags=[usuario_tag],
         responses={"200": UsuarioViewSchema, "404": ErrorSchema})
def get_usuarios(query: UsuarioBuscaSchema):
    """Faz a busca por um Usuario a partir do seu nome.

    Retorna uma representação dos usuarios.
    """
    usuario_nome = query.nome
    logger.debug(f"Coletando dados sobre usuario #{usuario_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    usuario = session.query(Usuario).filter(Usuario.nome == usuario_nome).first()

    if not usuario:
        # se o fornecedor não foi encontrado
        error_msg = "Usuario não localizado no banco :/"
        logger.warning(f"Erro ao buscar o usuario '{usuario_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Usuario localizado: '{usuario.nome}'")
        # retorna a representação de fornecedor
        return apresenta_usuario(usuario), 200
    

@app.get('/usuarios', tags=[usuario_tag],
         responses={"200": ListagemUsuariosSchema, "404": ErrorSchema})
def get_usuario():
    """Faz a busca por todos os Usuarios cadastrados no banco de dados.

    Retorna uma representação da lista de usuarios.
    """
    
    logger.debug(f"Coletando usuarios ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    usuarios = session.query(Usuario).order_by(Usuario.nome.asc()).all()

    if not usuarios:
        # se não há usuarios cadastrados
        return {"usuarios": []}, 200
    else:
        logger.debug(f"%d usuarios econtrados" % len(usuarios))
        # retorna a representação do fornecedor
        print(usuarios)
        return apresenta_usuarios(usuarios), 200