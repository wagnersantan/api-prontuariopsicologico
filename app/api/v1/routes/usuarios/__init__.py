from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_usuarios():
    return {"message": "Lista de usuários"}

usuario_routes = router
