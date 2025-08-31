import json
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.paciente.paciente_schema import PacienteCreate, PacienteUpdate
from services.paciente.paciente_service import (
    criar_paciente_service,
    listar_pacientes_service,
    obter_paciente_service,
    atualizar_paciente_service,
    deletar_paciente_service
)
from core.database import SessionLocal

router = APIRouter(prefix="/pacientes", tags=["Pacientes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Criar paciente ---
@router.post("/", response_model=dict)
async def criar_paciente(paciente: PacienteCreate, db: Session = Depends(get_db)):
    novo_paciente = criar_paciente_service(db, paciente)
    return {
        "id": novo_paciente.id,
        "nome": novo_paciente.nome,
        "cpf": novo_paciente.cpf,
        "rg": novo_paciente.rg,
        "data_nascimento": novo_paciente.data_nascimento,
        "idade": novo_paciente.idade,
        "genero": novo_paciente.genero,
        "email": novo_paciente.email,
        "telefone": novo_paciente.telefone,
        "endereco": novo_paciente.endereco,
        "contato_emergencia": novo_paciente.contato_emergencia,
        "plano_saude": novo_paciente.plano_saude,
        "numero_carteirinha": novo_paciente.numero_carteirinha,
        "historico_atendimentos": novo_paciente.historico_atendimentos,
        "diagnosticos": novo_paciente.diagnosticos,
        "medicamentos": novo_paciente.medicamentos,
        "observacoes": novo_paciente.observacoes,
    }


# --- Listar todos os pacientes ---
@router.get("/", response_model=list[dict])
async def listar_pacientes(db: Session = Depends(get_db)):
    pacientes = listar_pacientes_service(db)
    return [
        {
            "id": p.id,
            "nome": p.nome,
            "cpf": p.cpf,
            "rg": p.rg,
            "data_nascimento": p.data_nascimento,
            "idade": p.idade,
            "genero": p.genero,
            "email": p.email,
            "telefone": p.telefone,
            "endereco": p.endereco,
            "contato_emergencia": p.contato_emergencia,
            "plano_saude": p.plano_saude,
            "numero_carteirinha": p.numero_carteirinha,
            "historico_atendimentos": p.get_historico_atendimentos(),
            "diagnosticos": p.get_diagnosticos(),
            "medicamentos": p.get_medicamentos(),
            "observacoes": p.observacoes,
        }
        for p in pacientes
    ]


# --- Obter paciente por ID ---
@router.get("/{id}", response_model=dict)
async def obter_paciente(id: int, db: Session = Depends(get_db)):
    paciente = obter_paciente_service(db, id)
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    return {
        "id": paciente.id,
        "nome": paciente.nome,
        "cpf": paciente.cpf,
        "rg": paciente.rg,
        "data_nascimento": paciente.data_nascimento,
        "idade": paciente.idade,
        "genero": paciente.genero,
        "email": paciente.email,
        "telefone": paciente.telefone,
        "endereco": paciente.endereco,
        "contato_emergencia": paciente.contato_emergencia,
        "plano_saude": paciente.plano_saude,
        "numero_carteirinha": paciente.numero_carteirinha,
        "historico_atendimentos": paciente.get_historico_atendimentos(),
        "diagnosticos": paciente.get_diagnosticos(),
        "medicamentos": paciente.get_medicamentos(),
        "observacoes": paciente.observacoes,
    }

# --- Atualizar paciente ---
@router.put("/{id}", response_model=dict)
async def atualizar_paciente(id: int, paciente: PacienteUpdate, db: Session = Depends(get_db)):
    dados = {k: v for k, v in paciente.dict(exclude_unset=True).items() if v is not None}
    
    # Serializar listas em JSON
    for campo in ["historico_atendimentos", "diagnosticos", "medicamentos"]:
        if campo in dados:
            dados[campo] = json.dumps(dados[campo])
    
    paciente_atualizado = atualizar_paciente_service(db, id, dados)
    
    if not paciente_atualizado:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    
    # Retorno completo
    return {
        "id": paciente_atualizado.id,
        "nome": paciente_atualizado.nome,
        "cpf": paciente_atualizado.cpf,
        "rg": paciente_atualizado.rg,
        "data_nascimento": paciente_atualizado.data_nascimento,
        "idade": paciente_atualizado.idade,
        "genero": paciente_atualizado.genero,
        "email": paciente_atualizado.email,
        "telefone": paciente_atualizado.telefone,
        "endereco": paciente_atualizado.endereco,
        "contato_emergencia": paciente_atualizado.contato_emergencia,
        "plano_saude": paciente_atualizado.plano_saude,
        "numero_carteirinha": paciente_atualizado.numero_carteirinha,
        "historico_atendimentos": paciente_atualizado.get_historico_atendimentos(),
        "diagnosticos": paciente_atualizado.get_diagnosticos(),
        "medicamentos": paciente_atualizado.get_medicamentos(),
        "observacoes": paciente_atualizado.observacoes,
    }

# --- Deletar paciente ---
@router.delete("/{id}", response_model=dict)
async def deletar_paciente(id: int, db: Session = Depends(get_db)):
    paciente = deletar_paciente_service(db, id)
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    return {
        "mensagem": "Paciente deletado com sucesso",
        "paciente": {
            "id": paciente.id,
            "nome": paciente.nome,
            "cpf": paciente.cpf,
            "rg": paciente.rg,
            "data_nascimento": paciente.data_nascimento,
            "idade": paciente.idade,
            "genero": paciente.genero,
            "email": paciente.email,
            "telefone": paciente.telefone,
            "endereco": paciente.endereco,
            "contato_emergencia": paciente.contato_emergencia,
            "plano_saude": paciente.plano_saude,
            "numero_carteirinha": paciente.numero_carteirinha,
            "historico_atendimentos": paciente.get_historico_atendimentos(),
            "diagnosticos": paciente.get_diagnosticos(),
            "medicamentos": paciente.get_medicamentos(),
            "observacoes": paciente.observacoes,
        }
    }
