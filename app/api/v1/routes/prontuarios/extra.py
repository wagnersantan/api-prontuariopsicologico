from fastapi import APIRouter

router = APIRouter()

@router.get("/paciente/{id}")
async def prontuarios_paciente(id: int):
    return {"msg": f"Listar todos os prontuários do paciente {id}"}

@router.get("/versoes/{id}")
async def historico_prontuario(id: int):
    return {"msg": f"Histórico de alterações do prontuário {id}"}
