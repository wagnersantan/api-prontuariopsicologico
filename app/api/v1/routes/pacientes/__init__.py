from fastapi import APIRouter

router = APIRouter()

# Exemplo de rota
@router.get("/")
def read_pacientes():
    return {"message": "Lista de pacientes"}

# Exporte o router
paciente_routes = router
