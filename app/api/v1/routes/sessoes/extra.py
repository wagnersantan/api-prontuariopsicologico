from fastapi import APIRouter

router = APIRouter()

@router.get("/paciente/{id}")
async def sessoes_paciente(id: int):
    return {"msg": f"Listar todas as sessões do paciente {id}"}

@router.get("/psicologo/{id}")
async def sessoes_psicologo(id: int):
    return {"msg": f"Listar agenda completa do psicólogo {id}"}

@router.post("/{id}/cancelar")
async def cancelar_sessao(id: int):
    return {"msg": f"Cancelar ou reagendar sessão {id}"}
