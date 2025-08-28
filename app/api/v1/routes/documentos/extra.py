from fastapi import APIRouter

router = APIRouter()

@router.get("/paciente/{id}")
async def documentos_paciente(id: int):
    return {"msg": f"Listar documentos do paciente {id}"}

@router.post("/{id}/compartilhar")
async def compartilhar_documento(id: int):
    return {"msg": f"Compartilhar documento {id} com paciente ou outro psicólogo"}
