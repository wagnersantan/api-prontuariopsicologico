from pydantic import BaseModel
from typing import Optional

class ProntuarioCreate(BaseModel):
    paciente_id: int
    descricao: str

class ProntuarioUpdate(BaseModel):
    descricao: Optional[str] = None

class ProntuarioOut(BaseModel):
    id: int
    paciente_id: int
    descricao: str
