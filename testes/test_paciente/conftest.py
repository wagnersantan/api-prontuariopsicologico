# testes/conftest.py
import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture(scope="function")
def client():
    """
    Fixture que cria um cliente de teste para a API.
    O banco de dados é limpo automaticamente a cada teste.
    """
    with TestClient(app) as c:
        yield c
