from models.documento.documento_model import Documento

db = []
contador_id = 1

def criar_documento(documento: Documento):
    global contador_id
    documento.id = contador_id
    db.append(documento)
    contador_id += 1
    return documento

def listar_documentos():
    return db

def obter_documento(id: int):
    for d in db:
        if d.id == id:
            return d
    return None

def atualizar_documento(id: int, dados: dict):
    documento = obter_documento(id)
    if documento:
        for key, value in dados.items():
            setattr(documento, key, value)
    return documento

def deletar_documento(id: int):
    global db
    documento = obter_documento(id)
    if documento:
        db = [d for d in db if d.id != id]
    return documento
