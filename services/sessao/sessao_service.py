from repositories.sessao.sessao_repository import (
    criar_sessao,
    listar_sessoes,
    obter_sessao,
    atualizar_sessao,
    deletar_sessao
)
from models.sessao.sessao_model import Sessao

def criar_sessao_service(paciente_id, data, observacoes):
    sessao = Sessao(id=0, paciente_id=paciente_id, data=data, observacoes=observacoes)
    return criar_sessao(sessao)

def listar_sessoes_service():
    return listar_sessoes()

def obter_sessao_service(id: int):
    return obter_sessao(id)

def atualizar_sessao_service(id: int, dados: dict):
    return atualizar_sessao(id, dados)

def deletar_sessao_service(id: int):
    return deletar_sessao(id)
