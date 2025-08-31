# services/prontuario/prontuario_service.py

from repositories.prontuario.prontuario_repository import (
    criar_prontuario,
    listar_prontuarios,
    obter_prontuario,
    atualizar_prontuario,
    deletar_prontuario
)
from models.prontuario.prontuario_model import Prontuario

class ProntuarioService:
    def criar_prontuario(self, paciente_id, descricao):
        prontuario = Prontuario(paciente_id=paciente_id, descricao=descricao)
        return criar_prontuario(prontuario)

    def listar_prontuarios(self):
        return listar_prontuarios()

    def obter_prontuario(self, id: int):
        return obter_prontuario(id)

    def atualizar_prontuario(self, id: int, dados: dict):
        return atualizar_prontuario(id, dados)

    def deletar_prontuario(self, id: int):
        return deletar_prontuario(id)

# Mantendo as funções antigas para compatibilidade
criar_prontuario_service = ProntuarioService().criar_prontuario
listar_prontuarios_service = ProntuarioService().listar_prontuarios
obter_prontuario_service = ProntuarioService().obter_prontuario
atualizar_prontuario_service = ProntuarioService().atualizar_prontuario
deletar_prontuario_service = ProntuarioService().deletar_prontuario
