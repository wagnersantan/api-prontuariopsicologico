from sqlalchemy.orm import Session
from models.evolucao.evolucao_model import Evolucao

def criar_evolucao_repo(db: Session, evolucao: Evolucao):
    db.add(evolucao)
    db.commit()
    db.refresh(evolucao)
    return evolucao

def listar_evolucoes_repo(db: Session):
    return db.query(Evolucao).all()

def obter_evolucao_repo(db: Session, evolucao_id: int):
    return db.query(Evolucao).filter(Evolucao.id == evolucao_id).first()

def atualizar_evolucao_repo(db: Session, evolucao_id: int, dados: dict):
    evolucao = db.query(Evolucao).filter(Evolucao.id == evolucao_id).first()
    if evolucao:
        for key, value in dados.items():
            setattr(evolucao, key, value)
        db.commit()
        db.refresh(evolucao)
    return evolucao

def deletar_evolucao_repo(db: Session, evolucao_id: int):
    evolucao = db.query(Evolucao).filter(Evolucao.id == evolucao_id).first()
    if evolucao:
        db.delete(evolucao)
        db.commit()
    return evolucao
