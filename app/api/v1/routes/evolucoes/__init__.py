from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def listar_evolucoes():
    return {"message": "Lista de evoluções"}

@router.post("/")
def criar_evolucao():
    return {"message": "Evolução criada com sucesso"}

evolucao_routes = router
