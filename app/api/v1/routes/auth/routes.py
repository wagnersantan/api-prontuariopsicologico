from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
async def login():
    return {"mensagem": "Login realizado"}

@router.post("/logout")
async def logout():
    return {"mensagem": "Logout realizado"}

@router.post("/register")
async def registrar_psicologo():
    return {"mensagem": "Psicólogo cadastrado"}
