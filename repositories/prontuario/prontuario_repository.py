from models.prontuario.prontuario_model import Prontuario

db = []
contador_id = 1

def criar_prontuario(prontuario: Prontuario):
    global contador_id
    prontuario.id = contador_id
    db.append(prontuario)
    contador_id += 1
    return prontuario

def listar_prontuarios():
    return db

def obter_prontuario(id: int):
    for p in db:
        if p.id == id:
            return p
    return None

def atualizar_prontuario(id: int, dados: dict):
    prontuario = obter_prontuario(id)
    if prontuario:
        for key, value in dados.items():
            setattr(prontuario, key, value)
    return prontuario

def deletar_prontuario(id: int):
    global db
    prontuario = obter_prontuario(id)
    if prontuario:
        db = [p for p in db if p.id != id]
    return prontuario
