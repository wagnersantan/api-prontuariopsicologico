from fastapi import APIRouter

router = APIRouter()

@router.get("/paciente/{id}")
async def evolucoes_paciente(id: int):
    return {"msg": f"Listar todas as evoluções do paciente {id}"}
