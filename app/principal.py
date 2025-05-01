# app/principal.py

from fastapi import FastAPI
from app.rotas import pacientes, prontuarios  # Importando as rotas de pacientes e prontuários

app = FastAPI(
    title="API de Prontuário Psicológico",
    version="1.0.0",
    description="Esta API permite gerenciar prontuários psicológicos para integração com um aplicativo móvel."
)

# Incluindo as rotas

# Incluindo as rotas com prefixos
app.include_router(pacientes.router, prefix="/pacientes", tags=["Pacientes"])
app.include_router(prontuarios.router, prefix="/prontuarios", tags=["Prontuários"])

@app.get("/")
def verificar_funcionamento():
    return {"mensagem": "API de Prontuário Psicológico funcionando corretamente"}
