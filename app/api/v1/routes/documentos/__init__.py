from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_documentos():
    return {"message": "Lista de documentos"}

documento_routes = router
