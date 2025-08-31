# core/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ------------------------------
# Configuração do banco de dados
# ------------------------------
# Atualmente usando SQLite local.
# Para PostgreSQL, basta trocar a URL:
# postgresql+psycopg2://usuario:senha@host:porta/nome_do_banco
SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"

# Criação do engine do SQLAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}  # necessário apenas para SQLite
)

# Criação da sessão
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base para criação dos modelos
Base = declarative_base()

# ------------------------------
# Inicialização do banco
# ------------------------------
def init_db():
    """
    Importa os modelos e cria todas as tabelas no banco de dados.
    """
    import models.paciente.paciente_model
    import models.prontuario.prontuario_model
    import models.sessao.sessao_model
    import models.evolucao.evolucao_model
    import models.documento.documento_model
    import models.usuario.usuario_model

    Base.metadata.create_all(bind=engine)

# ------------------------------
# Função para injetar sessão no FastAPI
# ------------------------------
def get_db():
    """
    Retorna uma sessão do banco de dados para ser usada nas rotas.
    Garante que a sessão será fechada após o uso.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
