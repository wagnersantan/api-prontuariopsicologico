from datetime import date
import pytest
from models.paciente.paciente_model import Paciente

# ------------------------------
# Testes do modelo Paciente
# ------------------------------

def test_criar_paciente_modelo():
    paciente = Paciente(
        nome="João Silva",
        email="joao@teste.com",
        data_nascimento=date(1993, 5, 10)
    )
    assert paciente.nome == "João Silva"
    assert paciente.email == "joao@teste.com"
    assert paciente.data_nascimento == date(1993, 5, 10)
    # Campos opcionais podem ser testados como None
    assert paciente.cpf is None
    assert paciente.rg is None
    assert paciente.telefone is None
    assert paciente.endereco is None

# ------------------------------
# Testes do "service" simulado
# ------------------------------

def test_criar_paciente_service_simulado():
    # Mock simples de banco de dados
    class MockDB:
        def add(self, obj):
            self.obj = obj
        def commit(self):
            return True
        def refresh(self, obj):
            obj.id = 1
            return obj

    db = MockDB()

    paciente_data = Paciente(
        nome="Maria",
        email="maria@teste.com",
        data_nascimento=date(1998, 8, 20)
    )

    # Simulando a adição e commit
    db.add(paciente_data)
    db.commit()
    db.refresh(paciente_data)

    assert paciente_data.id == 1
    assert paciente_data.nome == "Maria"
    assert paciente_data.email == "maria@teste.com"
