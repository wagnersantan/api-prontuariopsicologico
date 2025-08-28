from pydantic import BaseModel, EmailStr
from typing import Optional, List, Any
from datetime import date

# Schema para criação de paciente
class PacienteCreate(BaseModel):
    nome: str
    cpf: Optional[str] = None
    rg: Optional[str] = None
    data_nascimento: Optional[date] = None
    genero: Optional[str] = None
    email: Optional[EmailStr] = None
    telefone: Optional[str] = None
    endereco: Optional[str] = None
    contato_emergencia: Optional[str] = None
    plano_saude: Optional[str] = None
    numero_carteirinha: Optional[str] = None
    historico_atendimentos: Optional[List[Any]] = None
    diagnosticos: Optional[List[Any]] = None
    medicamentos: Optional[List[Any]] = None
    observacoes: Optional[str] = None

    class Config:
        from_attributes = True  # substitui orm_mode = True no Pydantic V2

# Schema para atualização (todos opcionais)
class PacienteUpdate(BaseModel):
    nome: Optional[str] = None
    cpf: Optional[str] = None
    rg: Optional[str] = None
    data_nascimento: Optional[date] = None
    genero: Optional[str] = None
    email: Optional[EmailStr] = None
    telefone: Optional[str] = None
    endereco: Optional[str] = None
    contato_emergencia: Optional[str] = None
    plano_saude: Optional[str] = None
    numero_carteirinha: Optional[str] = None
    historico_atendimentos: Optional[List[Any]] = None
    diagnosticos: Optional[List[Any]] = None
    medicamentos: Optional[List[Any]] = None
    observacoes: Optional[str] = None

    class Config:
        from_attributes = True

# Schema para resposta da API
class PacienteOut(BaseModel):
    id: int
    nome: str
    cpf: Optional[str] = None
    rg: Optional[str] = None
    data_nascimento: Optional[date] = None
    genero: Optional[str] = None
    email: Optional[EmailStr] = None
    telefone: Optional[str] = None
    endereco: Optional[str] = None
    contato_emergencia: Optional[str] = None
    plano_saude: Optional[str] = None
    numero_carteirinha: Optional[str] = None
    historico_atendimentos: Optional[List[Any]] = None
    diagnosticos: Optional[List[Any]] = None
    medicamentos: Optional[List[Any]] = None
    observacoes: Optional[str] = None

    class Config:
        from_attributes = True
