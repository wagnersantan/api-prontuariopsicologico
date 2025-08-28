# schemas/evolucao/evolucao_schema.py
from pydantic import BaseModel
from datetime import date

# Campos básicos de uma evolução
class EvolucaoBase(BaseModel):
    prontuario_id: int
    nota: str
    data: date | None = None  # opcional, se quiser registrar a data

# Schema usado para criar uma evolução
class EvolucaoCreate(EvolucaoBase):
    pass  # herdando tudo de EvolucaoBase

# Schema de resposta (retorna evolução com ID)
class EvolucaoResponse(EvolucaoBase):
    id: int  # id gerado pelo banco

    class Config:
        from_attributes = True  # substitui orm_mode no Pydantic v2
