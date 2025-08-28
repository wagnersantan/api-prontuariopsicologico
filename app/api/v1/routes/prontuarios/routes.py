from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def abrir_prontuario():
    return {"mensagem": "Prontuário aberto"}

@router.get("/")
async def listar_prontuarios():
    return {"mensagem": "Lista de prontuários"}

@router.get("/{id}")
async def consultar_prontuario(id: int):
    return {"mensagem": f"Dados do prontuário {id}"}

@router.put("/{id}")
async def atualizar_prontuario(id: int):
    return {"mensagem": f"Prontuário {id} atualizado"}

@router.patch("/{id}/encerrar")
async def encerrar_prontuario(id: int):
    return {"mensagem": f"Prontuário {id} encerrado"}
