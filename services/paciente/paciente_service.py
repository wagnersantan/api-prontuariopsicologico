from sqlalchemy.orm import Session
from repositories.paciente.paciente_repository import (
    criar_paciente,
    listar_pacientes,
    obter_paciente,
    atualizar_paciente,
    deletar_paciente
)
from schemas.paciente.paciente_schema import PacienteCreate
from models.paciente.paciente_model import Paciente
import json

# Criar paciente
def criar_paciente_service(db: Session, paciente: PacienteCreate):
    """
    Recebe um objeto Pydantic PacienteCreate,
    cria e salva um Paciente no banco via repositório.
    """
    # Converte listas para JSON antes de criar o ORM
    paciente_orm = Paciente(
        nome=paciente.nome,
        cpf=paciente.cpf,
        rg=paciente.rg,
        data_nascimento=paciente.data_nascimento,
        genero=paciente.genero,
        email=paciente.email,
        telefone=paciente.telefone,
        endereco=paciente.endereco,
        contato_emergencia=paciente.contato_emergencia,
        plano_saude=paciente.plano_saude,
        numero_carteirinha=paciente.numero_carteirinha,
        historico_atendimentos=json.dumps(paciente.historico_atendimentos or []),
        diagnosticos=json.dumps(paciente.diagnosticos or []),
        medicamentos=json.dumps(paciente.medicamentos or []),
        observacoes=paciente.observacoes
    )
    return criar_paciente(db, paciente_orm)

# Listar todos os pacientes
def listar_pacientes_service(db: Session):
    return listar_pacientes(db)

# Obter paciente por id
def obter_paciente_service(db: Session, id: int):
    return obter_paciente(db, id)

# Atualizar paciente
def atualizar_paciente_service(db: Session, id: int, dados: dict):
    # Se alguma lista vier em dados, converte para JSON
    for key in ['historico_atendimentos', 'diagnosticos', 'medicamentos']:
        if key in dados and isinstance(dados[key], list):
            dados[key] = json.dumps(dados[key])
    return atualizar_paciente(db, id, dados)

# Deletar paciente
def deletar_paciente_service(db: Session, id: int):
    return deletar_paciente(db, id)
