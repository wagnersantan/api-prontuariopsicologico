from sqlalchemy import Column, Integer, String, Text, Date
from core.database import Base
import json

class Paciente(Base):
    __tablename__ = "pacientes"

    # Identificação básica
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    cpf = Column(String, unique=True, index=True, nullable=True)  # identificação oficial
    rg = Column(String, nullable=True)

    # Dados pessoais
    data_nascimento = Column(Date, nullable=True)  # use ISO format no Pydantic
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

    # Métodos auxiliares para converter listas para JSON ao salvar
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
