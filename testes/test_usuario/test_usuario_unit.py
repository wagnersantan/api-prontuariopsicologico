import pytest
from models.usuario.usuario_model import Usuario

@pytest.mark.unit
class TestUsuario:

    def test_criar_usuario_modelo(self):
        usuario = Usuario(nome="Ana")
        assert usuario.nome == "Ana"

    def test_criar_usuario_service_simulado(self):
        class MockDB:
            def add(self, obj):
                self.obj = obj
            def commit(self):
                return True
            def refresh(self, obj):
                obj.id = 1
                return obj

        db = MockDB()
        usuario_data = Usuario(nome="Bruno")
        db.add(usuario_data)
        db.commit()
        db.refresh(usuario_data)
        assert usuario_data.id == 1
