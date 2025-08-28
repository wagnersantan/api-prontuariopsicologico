from fastapi import APIRouter

router = APIRouter()

# -------------------------------
# Rotas para sessões de um prontuário
# -------------------------------

@router.post("/prontuario/{prontuario_id}")
async def registrar_sessao(prontuario_id: int):
    return {"mensagem": f"Sessão registrada para prontuário {prontuario_id}"}

@router.get("/prontuario/{prontuario_id}")
async def listar_sessoes(prontuario_id: int):
    return {"mensagem": f"Lista de sessões do prontuário {prontuario_id}"}

# -------------------------------
# Rotas para uma sessão específica
# -------------------------------

@router.get("/sessao/{sessao_id}")
async def consultar_sessao(sessao_id: int):
    return {"mensagem": f"Consulta da sessão {sessao_id}"}

@router.put("/sessao/{sessao_id}")
async def atualizar_sessao(sessao_id: int):
    return {"mensagem": f"Sessão {sessao_id} atualizada"}

@router.delete("/sessao/{sessao_id}")
async def deletar_sessao(sessao_id: int):
    return {"mensagem": f"Sessão {sessao_id} excluída"}
