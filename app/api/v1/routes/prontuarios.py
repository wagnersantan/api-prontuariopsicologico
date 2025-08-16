from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from core.database import SessionLocal
from models.prontuario import Prontuario
from schemas.prontuario import Prontuario as ProntuarioSchema

router = APIRouter()

# Dependência para abrir/fechar sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1️⃣ Listar todos os prontuários
@router.get("/", response_model=List[ProntuarioSchema])
def listar_prontuarios(db: Session = Depends(get_db)):
    prontuarios = db.query(Prontuario).all()
    return prontuarios

# 2️⃣ Criar prontuário
@router.post("/", response_model=ProntuarioSchema)
def criar_prontuario(prontuario: ProntuarioSchema, db: Session = Depends(get_db)):
    novo_prontuario = Prontuario(
        paciente_id=prontuario.paciente_id,
        descricao=prontuario.descricao,
        data=prontuario.data
    )
    db.add(novo_prontuario)
    db.commit()
    db.refresh(novo_prontuario)
    return novo_prontuario

# 3️⃣ Buscar prontuário por ID
@router.get("/{prontuario_id}", response_model=ProntuarioSchema)
def buscar_prontuario(prontuario_id: int, db: Session = Depends(get_db)):
    prontuario = db.query(Prontuario).filter(Prontuario.id == prontuario_id).first()
    if not prontuario:
        raise HTTPException(status_code=404, detail="Prontuário não encontrado")
    return prontuario
