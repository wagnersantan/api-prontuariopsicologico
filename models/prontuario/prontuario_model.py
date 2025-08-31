# models/prontuario.py
from sqlalchemy import Column, Integer, ForeignKey, Boolean, String
from sqlalchemy.orm import relationship
from core.database import Base

class Prontuario(Base):
    __tablename__ = "prontuarios"

    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"))
    ativo = Column(Boolean, default=True)
    descricao = Column(String, default="")  # campo de exemplo

    # Relacionamento com Paciente
    paciente = relationship("Paciente", back_populates="prontuarios")
