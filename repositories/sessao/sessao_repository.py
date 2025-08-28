from models.sessao.sessao_model import Sessao

db = []
contador_id = 1

def criar_sessao(sessao: Sessao):
    global contador_id
    sessao.id = contador_id
    db.append(sessao)
    contador_id += 1
    return sessao

def listar_sessoes():
    return db

def obter_sessao(id: int):
    for s in db:
        if s.id == id:
            return s
    return None

def atualizar_sessao(id: int, dados: dict):
    sessao = obter_sessao(id)
    if sessao:
        for key, value in dados.items():
            setattr(sessao, key, value)
    return sessao

def deletar_sessao(id: int):
    global db
    sessao = obter_sessao(id)
    if sessao:
        db = [s for s in db if s.id != id]
    return sessao
