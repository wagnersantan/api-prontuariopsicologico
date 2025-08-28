from fastapi import APIRouter

router = APIRouter()

@router.get("/sessoes/hoje")
async def alertas_sessoes_hoje():
    return {"msg": "Lembretes de sessões do dia para o psicólogo"}

@router.get("/pacientes/sem-atendimento")
async def alertas_pacientes_sem_atendimento():
    return {"msg": "Pacientes sem sessão há X dias"}

@router.get("/estatisticas/progresso/paciente/{id}")
async def progresso_paciente(id: int):
    return {"msg": f"Gráfico de evolução do paciente {id}"}

@router.get("/estatisticas/progresso/psicologo/{id}")
async def progresso_psicologo(id: int):
    return {"msg": f"Resumo de progresso de todos os pacientes do psicólogo {id}"}
