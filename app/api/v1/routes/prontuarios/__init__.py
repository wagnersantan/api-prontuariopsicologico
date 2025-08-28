from fastapi import APIRouter

router = APIRouter()

# Exemplo de rota
@router.get("/")
def read_prontuarios():
    return {"message": "Lista de prontuários"}

# Exporta o router para o main.py
prontuario_routes = router
