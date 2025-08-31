import pytest
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# Base de teste
Base = declarative_base()

# Classe mínima Paciente só para o teste
class Paciente(Base):
    __tablename__ = "pacientes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, default="Paciente Teste")

# Modelo Prontuario
class Prontuario(Base):
    __tablename__ = "prontuarios"
    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"))
    ativo = Column(Boolean, default=True)
    paciente = relationship("Paciente", backref="prontuarios")

# Serviço de Prontuario
class ProntuarioService:
    def __init__(self, db_session):
        self.db = db_session

    def criar_prontuario(self, paciente_id: int, descricao: str):
        prontuario = Prontuario(paciente_id=paciente_id)
        self.db.add(prontuario)
        self.db.commit()
        self.db.refresh(prontuario)
        return prontuario

# Fixture do banco em memória
@pytest.fixture
def db_session():
    engine = create_engine("sqlite:///:memory:", echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    # Cria paciente mínimo
    paciente = Paciente()
    session.add(paciente)
    session.commit()
    yield session
    session.close()

@pytest.mark.unit
class TestProntuario:
    def test_criar_prontuario_modelo(self, db_session):
        prontuario = Prontuario(paciente_id=1)
        db_session.add(prontuario)
        db_session.commit()
        db_session.refresh(prontuario)
        assert prontuario.paciente_id == 1
        assert prontuario.ativo is True

    def test_criar_prontuario_service(self, db_session):
        service = ProntuarioService(db_session)
        prontuario = service.criar_prontuario(paciente_id=1, descricao="Consulta Inicial")
        assert isinstance(prontuario, Prontuario)
        assert prontuario.id == 1
