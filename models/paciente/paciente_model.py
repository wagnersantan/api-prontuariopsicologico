# models/paciente.py
from sqlalchemy import Column, Integer, String, Text, Date
from sqlalchemy.orm import relationship
from core.database import Base
import json
from datetime import date

class Paciente(Base):
    __tablename__ = "pacientes"

    # Identificação básica
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, unique=True, index=True, nullable=True)
    rg = Column(String, nullable=True)

    # Dados pessoais
    data_nascimento = Column(Date, nullable=True)
    idade = Column(Integer, nullable=True)  # <-- nova coluna
    genero = Column(String, nullable=True)

    # Contato
    email = Column(String, unique=True, index=True, nullable=True)
    telefone = Column(String, nullable=True)
    endereco = Column(String, nullable=True)
    contato_emergencia = Column(String, nullable=True)

    # Dados administrativos
    plano_saude = Column(String, nullable=True)
    numero_carteirinha = Column(String, nullable=True)

    # Dados clínicos (armazenados como JSON em texto)
    historico_atendimentos = Column(Text, nullable=True)
    diagnosticos = Column(Text, nullable=True)
    medicamentos = Column(Text, nullable=True)
    observacoes = Column(Text, nullable=True)

    # Relacionamento com Prontuarios
    prontuarios = relationship("Prontuario", back_populates="paciente")

    # Métodos auxiliares para converter listas para JSON
    def set_historico_atendimentos(self, lista):
        self.historico_atendimentos = json.dumps(lista)

    def get_historico_atendimentos(self):
        if self.historico_atendimentos:
            return json.loads(self.historico_atendimentos)
        return []

    def set_diagnosticos(self, lista):
        self.diagnosticos = json.dumps(lista)

    def get_diagnosticos(self):
        if self.diagnosticos:
            return json.loads(self.diagnosticos)
        return []

    def set_medicamentos(self, lista):
        self.medicamentos = json.dumps(lista)

    def get_medicamentos(self):
        if self.medicamentos:
            return json.loads(self.medicamentos)
        return []

    # Método opcional para calcular idade a partir da data de nascimento
    def calcular_idade(self):
        if self.data_nascimento:
            today = date.today()
            return today.year - self.data_nascimento.year - (
                (today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day)
            )
        return None
