from sqlalchemy import Column, Integer, String, ForeignKey, Date
from core.database import Base

class Prontuario(Base):
    __tablename__ = "prontuarios"

    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("pacientes.id"), nullable=False)
    descricao = Column(String, nullable=False)
    data = Column(Date, nullable=False)
