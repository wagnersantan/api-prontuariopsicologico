from fastapi import APIRouter

router = APIRouter()

@router.get("/busca")
async def buscar_pacientes(nome: str = None, cpf: str = None, email: str = None):
    return {"msg": "Buscar pacientes por nome, CPF ou email"}

@router.get("/{id}/estatisticas")
async def estatisticas_paciente(id: int):
    return {"msg": f"Resumo do histórico e evolução do paciente {id}"}
