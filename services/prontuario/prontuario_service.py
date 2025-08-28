from repositories.prontuario.prontuario_repository import (
    criar_prontuario,
    listar_prontuarios,
    obter_prontuario,
    atualizar_prontuario,
    deletar_prontuario
)
from models.prontuario.prontuario_model import Prontuario

def criar_prontuario_service(paciente_id, descricao):
    prontuario = Prontuario(id=0, paciente_id=paciente_id, descricao=descricao)
    return criar_prontuario(prontuario)

def listar_prontuarios_service():
    return listar_prontuarios()

def obter_prontuario_service(id: int):
    return obter_prontuario(id)

def atualizar_prontuario_service(id: int, dados: dict):
    return atualizar_prontuario(id, dados)

def deletar_prontuario_service(id: int):
    return deletar_prontuario(id)
