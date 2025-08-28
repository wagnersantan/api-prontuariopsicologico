from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_sessoes():
    return {"message": "Lista de sessões"}

sessao_routes = router
