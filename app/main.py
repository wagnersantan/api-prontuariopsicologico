from fastapi import FastAPI
from core.config import settings
from core.database import init_db
from app.api.v1.routes import pacientes, prontuarios

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        description=settings.DESCRIPTION,
        debug=settings.DEBUG
    )

    # Inicializar banco
    init_db()

    # 🔹 Rota inicial para teste
    @app.get("/")
    def root():
        return {"message": f"{settings.PROJECT_NAME} está rodando!"}

    # Registrar rotas
    app.include_router(pacientes.router, prefix="/api/v1/pacientes", tags=["Pacientes"])
    app.include_router(prontuarios.router, prefix="/api/v1/prontuarios", tags=["Prontuários"])

    return app

app = create_app()
