from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from schemas.evolucao.evolucao_schema import EvolucaoCreate, EvolucaoResponse
from services.evolucao.evolucao_service import (
    criar_evolucao_service,
    listar_evolucoes_service,
    obter_evolucao_service,
    atualizar_evolucao_service,
    deletar_evolucao_service
)
from core.database import get_db

router = APIRouter()

# Criar evolução
@router.post("/{prontuario_id}/evolucoes", response_model=EvolucaoResponse)
def adicionar_evolucao(prontuario_id: int, evolucao: EvolucaoCreate, db: Session = Depends(get_db)):
    return criar_evolucao_service(db, prontuario_id, evolucao.nota)

# Listar evoluções de um prontuário
@router.get("/{prontuario_id}/evolucoes", response_model=List[EvolucaoResponse])
def listar_evolucoes(prontuario_id: int, db: Session = Depends(get_db)):
    evolucoes = listar_evolucoes_service(db)
    return [e for e in evolucoes if e.prontuario_id == prontuario_id]

# Obter evolução específica
@router.get("/{prontuario_id}/evolucoes/{evolucao_id}", response_model=EvolucaoResponse)
def obter_evolucao(prontuario_id: int, evolucao_id: int, db: Session = Depends(get_db)):
    evolucao = obter_evolucao_service(db, evolucao_id)
    if not evolucao or evolucao.prontuario_id != prontuario_id:
        raise HTTPException(status_code=404, detail="Evolução não encontrada")
    return evolucao

# Atualizar evolução
@router.put("/{prontuario_id}/evolucoes/{evolucao_id}", response_model=EvolucaoResponse)
def atualizar_evolucao(prontuario_id: int, evolucao_id: int, dados: EvolucaoCreate, db: Session = Depends(get_db)):
    evolucao = atualizar_evolucao_service(db, evolucao_id, dados.dict())
    if not evolucao or evolucao.prontuario_id != prontuario_id:
        raise HTTPException(status_code=404, detail="Evolução não encontrada")
    return evolucao

# Deletar evolução
@router.delete("/{prontuario_id}/evolucoes/{evolucao_id}")
def deletar_evolucao(prontuario_id: int, evolucao_id: int, db: Session = Depends(get_db)):
    evolucao = deletar_evolucao_service(db, evolucao_id)
    if not evolucao or evolucao.prontuario_id != prontuario_id:
        raise HTTPException(status_code=404, detail="Evolução não encontrada")
    return {"mensagem": "Evolução deletada com sucesso"}
