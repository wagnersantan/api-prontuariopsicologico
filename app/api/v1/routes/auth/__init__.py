from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
def login():
    return {"message": "Login realizado com sucesso"}

@router.post("/register")
def register():
    return {"message": "Registro realizado com sucesso"}

auth_routes = router
