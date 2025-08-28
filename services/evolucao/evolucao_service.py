from sqlalchemy.orm import Session
from models.evolucao.evolucao_model import Evolucao
from repositories.evolucao.evolucao_repository import (
    criar_evolucao_repo,
    listar_evolucoes_repo,
    obter_evolucao_repo,
    atualizar_evolucao_repo,
    deletar_evolucao_repo
)

def criar_evolucao_service(db: Session, prontuario_id: int, nota: str):
    nova_evolucao = Evolucao(prontuario_id=prontuario_id, nota=nota)
    return criar_evolucao_repo(db, nova_evolucao)

def listar_evolucoes_service(db: Session):
    return listar_evolucoes_repo(db)

def obter_evolucao_service(db: Session, evolucao_id: int):
    return obter_evolucao_repo(db, evolucao_id)

def atualizar_evolucao_service(db: Session, evolucao_id: int, dados: dict):
    return atualizar_evolucao_repo(db, evolucao_id, dados)

def deletar_evolucao_service(db: Session, evolucao_id: int):
    return deletar_evolucao_repo(db, evolucao_id)
