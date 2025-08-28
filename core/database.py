# core/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # necessário apenas para SQLite
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def init_db():
    import models.paciente.paciente_model
    import models.prontuario.prontuario_model
    import models.sessao.sessao_model
    import models.evolucao.evolucao_model
    import models.documento.documento_model
    import models.usuario.usuario_model

    Base.metadata.create_all(bind=engine)

# ✅ Função para injetar a sessão no FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
