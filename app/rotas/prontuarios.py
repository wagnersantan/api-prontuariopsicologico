# app/rotas/prontuarios.py

from fastapi import APIRouter
from app.esquemas.prontuario import Prontuario, Sessao
from app.esquemas.paciente import Paciente

router = APIRouter()

# Armazenamento simples em memória para sessões
prontuarios_db = {}

@router.post("/prontuarios")
def cadastrar_prontuario(prontuario: Prontuario):
    # Verificando se o paciente já existe
    if prontuario.paciente_id not in prontuarios_db:
        prontuarios_db[prontuario.paciente_id] = prontuario
        return {"mensagem": "Prontuário criado com sucesso", "prontuario": prontuario}
    return {"mensagem": "Prontuário já existe"}

@router.post("/prontuarios/{paciente_id}/sessao")
def adicionar_sessao(paciente_id: int, sessao: Sessao):
    # Verifica se o paciente possui prontuário
    if paciente_id not in prontuarios_db:
        return {"mensagem": "Paciente não encontrado"}
    
    prontuario = prontuarios_db[paciente_id]
    prontuario.sessoes.append(sessao)
    
    return {"mensagem": "Sessão adicionada com sucesso", "sessao": sessao}
