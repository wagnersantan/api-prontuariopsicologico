from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from core.database import Base

class Documento(Base):
    __tablename__ = "documentos"

    id = Column(Integer, primary_key=True, index=True)
    prontuario_id = Column(Integer, ForeignKey("prontuarios.id"))
    nome_arquivo = Column(String)
    caminho = Column(String)

    prontuario = relationship("Prontuario", backref="documentos")
