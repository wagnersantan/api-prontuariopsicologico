from sqlalchemy.orm import Session
from models.paciente.paciente_model import Paciente
import json

# Criar paciente
def criar_paciente(db: Session, paciente: Paciente):
    novo_paciente = Paciente(
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
    db.add(novo_paciente)
    db.commit()
    db.refresh(novo_paciente)
    return novo_paciente

# Listar todos os pacientes
def listar_pacientes(db: Session):
    return db.query(Paciente).all()

# Obter paciente por id
def obter_paciente(db: Session, id: int):
    return db.query(Paciente).filter(Paciente.id == id).first()

# Atualizar paciente
def atualizar_paciente(db: Session, id: int, dados: dict):
    paciente = obter_paciente(db, id)
    if paciente:
        for key, value in dados.items():
            # Se for lista, converte para JSON
            if key in ['historico_atendimentos', 'diagnosticos', 'medicamentos'] and isinstance(value, list):
                setattr(paciente, key, json.dumps(value))
            else:
                setattr(paciente, key, value)
        db.commit()
        db.refresh(paciente)
    return paciente

# Deletar paciente
def deletar_paciente(db: Session, id: int):
    paciente = obter_paciente(db, id)
    if paciente:
        db.delete(paciente)
        db.commit()
    return paciente
