from pydantic import BaseModel
from typing import Optional

class SessaoCreate(BaseModel):
    paciente_id: int
    data: str
    observacoes: str

class SessaoUpdate(BaseModel):
    data: Optional[str] = None
    observacoes: Optional[str] = None

class SessaoOut(BaseModel):
    id: int
    paciente_id: int
    data: str
    observacoes: str
