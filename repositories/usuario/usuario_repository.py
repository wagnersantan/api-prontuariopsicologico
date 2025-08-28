from models.usuario.usuario_model import Usuario

db = []
contador_id = 1

def criar_usuario(usuario: Usuario):
    global contador_id
    usuario.id = contador_id
    db.append(usuario)
    contador_id += 1
    return usuario

def listar_usuarios():
    return db

def obter_usuario(id: int):
    for u in db:
        if u.id == id:
            return u
    return None

def atualizar_usuario(id: int, dados: dict):
    usuario = obter_usuario(id)
    if usuario:
        for key, value in dados.items():
            setattr(usuario, key, value)
    return usuario

def deletar_usuario(id: int):
    global db
    usuario = obter_usuario(id)
    if usuario:
        db = [u for u in db if u.id != id]
    return usuario
