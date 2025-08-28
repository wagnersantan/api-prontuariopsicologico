from fastapi import APIRouter

router = APIRouter()

@router.post("/{prontuario_id}/documentos")
async def anexar_documento(prontuario_id: int):
    return {"mensagem": f"Documento anexado ao prontuário {prontuario_id}"}

@router.get("/{prontuario_id}/documentos")
async def listar_documentos(prontuario_id: int):
    return {"mensagem": f"Lista de documentos do prontuário {prontuario_id}"}

@router.get("/{id}")
async def baixar_documento(id: int):
    return {"mensagem": f"Download do documento {id}"}

@router.delete("/{id}")
async def remover_documento(id: int):
    return {"mensagem": f"Documento {id} removido"}
