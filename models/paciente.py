from sqlalchemy import Column, Integer, String
from core.database import Base  # ✅ Import ajustado

class Paciente(Base):
    __tablename__ = "pacientes"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    telefone = Column(String, nullable=True)

    def __repr__(self):
        return f"<Paciente(id={self.id}, nome={self.nome})>"
