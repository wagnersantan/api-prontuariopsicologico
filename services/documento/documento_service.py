from repositories.documento.documento_repository import (
    criar_documento,
    listar_documentos,
    obter_documento,
    atualizar_documento,
    deletar_documento
)
from models.documento.documento_model import Documento

def criar_documento_service(prontuario_id, nome, conteudo):
    documento = Documento(id=0, prontuario_id=prontuario_id, nome=nome, conteudo=conteudo)
    return criar_documento(documento)

def listar_documentos_service():
    return listar_documentos()

def obter_documento_service(id: int):
    return obter_documento(id)

def atualizar_documento_service(id: int, dados: dict):
    return atualizar_documento(id, dados)

def deletar_documento_service(id: int):
    return deletar_documento(id)
