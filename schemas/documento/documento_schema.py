from pydantic import BaseModel
from typing import Optional

class DocumentoCreate(BaseModel):
    prontuario_id: int
    nome: str
    conteudo: str

class DocumentoUpdate(BaseModel):
    nome: Optional[str] = None
    conteudo: Optional[str] = None

class DocumentoOut(BaseModel):
    id: int
    prontuario_id: int
    nome: str
    conteudo: str
