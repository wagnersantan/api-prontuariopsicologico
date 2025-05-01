# app/esquemas/prontuario.py
from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class Sessao(BaseModel):
    data: date
    duracao_em_minutos: int
    observacoes: str

class Prontuario(BaseModel):
    paciente_id: int  # Referência ao paciente
    sessoes: List[Sessao] = []  # Lista de sessões de um prontuário

    class Config:
        orm_mode = True
