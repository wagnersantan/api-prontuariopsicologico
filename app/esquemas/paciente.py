# app/esquemas/paciente.py

from pydantic import BaseModel
from typing import Optional

class Paciente(BaseModel):
    nome: str
    idade: int
    sexo: str
    telefone: Optional[str] = None  # Não obrigatório
    endereco: Optional[str] = None  # Não obrigatório

    class Config:
        orm_mode = True
