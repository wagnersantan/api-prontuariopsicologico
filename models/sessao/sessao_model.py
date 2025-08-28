from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship
from core.database import Base
from datetime import datetime

class Sessao(Base):
    __tablename__ = "sessoes"

    id = Column(Integer, primary_key=True, index=True)
    prontuario_id = Column(Integer, ForeignKey("prontuarios.id"))
    resumo = Column(String)
    data = Column(DateTime, default=datetime.utcnow)

    prontuario = relationship("Prontuario", backref="sessoes")
