from fastapi import APIRouter

router = APIRouter()

@router.post("/ativar")
async def ativar_usuario():
    return {"msg": "Ativar psicólogo ou usuário"}

@router.post("/desativar")
async def desativar_usuario():
    return {"msg": "Desativar psicólogo ou usuário"}

@router.get("/permissoes/{id}")
async def permissoes_usuario(id: int):
    return {"msg": f"Ver permissões e acessos do usuário {id}"}
