from pathlib import Path

class Settings:
    # Configurações gerais
    PROJECT_NAME: str = "API de Prontuário Psicológico"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "API para gestão de pacientes e prontuários (ambiente local)."

    # Caminho base do projeto
    BASE_DIR: Path = Path(__file__).resolve().parent.parent

    # Configuração do banco (SQLite local)
    DATABASE_URL: str = f"sqlite:///{BASE_DIR}/database.db"

    # Configurações adicionais
    DEBUG: bool = True

# Instância única para ser importada no resto do projeto
settings = Settings()
