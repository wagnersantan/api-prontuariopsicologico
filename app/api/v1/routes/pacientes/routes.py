import json
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

# Schemas
from schemas.paciente.paciente_schema import PacienteCreate, PacienteUpdate

# Services
from services.paciente.paciente_service import (
    criar_paciente_service,
    listar_pacientes_service,
    obter_paciente_service,
    atualizar_paciente_service,
    deletar_paciente_service
)

# Database
from core.database import SessionLocal

router = APIRouter(prefix="/pacientes", tags=["Pacientes"])

# Dependência para criar a sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Criar paciente ---
@router.post("/")
async def criar_paciente(paciente: PacienteCreate, db: Session = Depends(get_db)):
    novo_paciente = criar_paciente_service(db, paciente)
    return novo_paciente

# --- Listar todos os pacientes ---
@router.get("/")
async def listar_pacientes(db: Session = Depends(get_db)):
    return listar_pacientes_service(db)

# --- Obter paciente por ID ---
@router.get("/{id}")
async def obter_paciente(id: int, db: Session = Depends(get_db)):
    paciente = obter_paciente_service(db, id)
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    return paciente

# --- Atualizar paciente ---
@router.put("/{id}")
async def atualizar_paciente(id: int, paciente: PacienteUpdate, db: Session = Depends(get_db)):
    dados = {k: v for k, v in paciente.dict(exclude_unset=True).items() if v is not None}

    # Serializa listas/dicts em JSON, se houver
    for campo in ["historico_atendimentos", "diagnosticos", "medicamentos"]:
        if campo in dados:
            dados[campo] = json.dumps(dados[campo])

    paciente_atualizado = atualizar_paciente_service(db, id, dados)
    if not paciente_atualizado:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    return paciente_atualizado

# --- Deletar paciente ---
@router.delete("/{id}")
async def deletar_paciente(id: int, db: Session = Depends(get_db)):
    paciente = deletar_paciente_service(db, id)
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    return {"mensagem": "Paciente deletado com sucesso"}
