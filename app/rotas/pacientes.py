# app/rotas/pacientes.py

from fastapi import APIRouter
from app.esquemas.paciente import Paciente

router = APIRouter()

# Lista para armazenar pacientes em memória (exemplo simples)
pacientes_db = []

@router.post("/pacientes")
def cadastrar_paciente(paciente: Paciente):
    pacientes_db.append(paciente)
    return {"mensagem": "Paciente cadastrado com sucesso", "paciente": paciente}
