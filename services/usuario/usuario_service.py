from repositories.usuario.usuario_repository import (
    criar_usuario,
    listar_usuarios,
    obter_usuario,
    atualizar_usuario,
    deletar_usuario
)
from models.usuario.usuario_model import Usuario

def criar_usuario_service(nome, email, senha):
    usuario = Usuario(id=0, nome=nome, email=email, senha=senha)
    return criar_usuario(usuario)

def listar_usuarios_service():
    return listar_usuarios()

def obter_usuario_service(id: int):
    return obter_usuario(id)

def atualizar_usuario_service(id: int, dados: dict):
    return atualizar_usuario(id, dados)

def deletar_usuario_service(id: int):
    return deletar_usuario(id)
