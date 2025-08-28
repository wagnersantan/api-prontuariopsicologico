from fastapi import FastAPI

# Importando os routers
#from app.api.v1.routes.pacientes import paciente_routes
#from app.api.v1.routes.documentos import documento_routes
#from app.api.v1.routes.usuarios import usuario_routes

# Criando a aplicação FastAPI
#app = FastAPI(title="API Prontuário Psicológico")

# Incluindo os routers com prefixos e tags
#app.include_router(paciente_routes, prefix="/pacientes", tags=["Pacientes"])
#app.include_router(prontuario_routes, prefix="/prontuarios", tags=["Prontuários"])
#app.include_router(documento_routes, prefix="/documentos", tags=["Documentos"])
#app.include_router(usuario_routes, prefix="/usuarios", tags=["Usuários"])


#from fastapi import FastAPI

#from app.api.v1.routes.pacientes.routes import router as paciente_routes
#from app.api.v1.routes.prontuarios.routes import router as prontuario_routes
#from app.api.v1.routes.documentos.routes import router as documento_routes
#from app.api.v1.routes.usuarios.usuario_routes import router as usuario_routes

#app = FastAPI(title="API Prontuário Psicológico")

#app.include_router(paciente_routes, prefix="/pacientes", tags=["Pacientes"])
#app.include_router(prontuario_routes, prefix="/prontuarios", tags=["Prontuários"])
#app.include_router(documento_routes, prefix="/documentos", tags=["Documentos"])
#app.include_router(usuario_routes, prefix="/usuarios", tags=["Usuários"])


from fastapi import FastAPI

# Importando routers
from app.api.v1.routes.pacientes.routes import router as paciente_routes
from app.api.v1.routes.prontuarios.routes import router as prontuario_routes
from app.api.v1.routes.documentos.routes import router as documento_routes
from app.api.v1.routes.usuarios.usuario_routes import router as usuario_routes
from app.api.v1.routes.sessoes.routes import router as sessoes_routes
from app.api.v1.routes.evolucoes.routes import router as evolucao_routes

# Importando função para inicializar o banco
from core.database import init_db

# Criando app FastAPI
app = FastAPI(title="API Prontuário Psicológico")

# Inicializa o banco e cria todas as tabelas
init_db()

# Incluindo routers
app.include_router(paciente_routes)
app.include_router(prontuario_routes)
app.include_router(documento_routes)
app.include_router(usuario_routes)
app.include_router(sessoes_routes)
app.include_router(evolucao_routes)
