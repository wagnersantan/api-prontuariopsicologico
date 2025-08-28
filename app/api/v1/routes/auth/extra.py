from fastapi import APIRouter

router = APIRouter()

@router.post("/auth/refresh-token")
async def refresh_token():
    return {"msg": "Renovar token JWT"}

@router.post("/auth/recuperar-senha")
async def recuperar_senha(email: str):
    return {"msg": f"Processo de recuperação de senha para {email}"}
