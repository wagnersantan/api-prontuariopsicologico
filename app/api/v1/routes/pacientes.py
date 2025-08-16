from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from core.database import SessionLocal  # corrigido
from models.paciente import Paciente    # corrigido
from schemas.paciente import Paciente as PacienteSchema  # corrigido

router = APIRouter()

# Dependência para abrir/fechar sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1️⃣ Listar todos os pacientes
@router.get("/", response_model=List[PacienteSchema])
def listar_pacientes(db: Session = Depends(get_db)):
    pacientes = db.query(Paciente).all()
    return pacientes

# 2️⃣ Criar paciente
@router.post("/", response_model=PacienteSchema)
def criar_paciente(paciente: PacienteSchema, db: Session = Depends(get_db)):
    novo_paciente = Paciente(
        nome=paciente.nome,
        email=paciente.email,
        telefone=paciente.telefone
    )
    db.add(novo_paciente)
    db.commit()
    db.refresh(novo_paciente)
    return novo_paciente

# 3️⃣ Buscar paciente por ID
@router.get("/{paciente_id}", response_model=PacienteSchema)
def buscar_paciente(paciente_id: int, db: Session = Depends(get_db)):
    paciente = db.query(Paciente).filter(Paciente.id == paciente_id).first()
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    return paciente
