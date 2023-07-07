from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime, date
from typing import Union

from model import Base

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column("pk_usuario", Integer, primary_key=True)
    nome = Column(String(20))
    sobrenome = Column(String(50))
    cpf = Column(String(20))
    data_nascimento = Column(String(20))
    email = Column(String)
    login = Column(String)
    senha = Column(String)
    senha_novamente = Column(String)
    data_insercao = Column(DateTime, default=datetime.now())


    def __init__(self, nome:str, sobrenome:str, cpf:str, data_nascimento:date, email:str, login:str, senha:str, senha_novamente:str,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Usuario

        Arguments:
            
            nome: primeiro nome do usuario a ser criado.
            sobrenome: segundo nome do usuario.
            cpf: cpf do usuario.
            data_nascimento: data de nascimento do usuario.
            email: email para contato do usuario
            login: login de acesso ao usuario
            senha: senha do usuario
            senha_novamente: confirmação de senha do usuario
            data_insercao: data de quando o usuario foi inserido à base
        """
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.email = email
        self.login = login
        self.senha = senha
        self.senha_novamente = senha_novamente
        

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao
        
    