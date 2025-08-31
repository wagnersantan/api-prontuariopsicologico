import pytest
from models.sessao.sessao_model import Sessao
from datetime import datetime

@pytest.mark.unit
class TestSessao:

    def test_criar_sessao_modelo(self):
        # usamos os campos existentes: prontuario_id e resumo
        sessao = Sessao(prontuario_id=1, resumo="Terapia Cognitiva")
        assert sessao.prontuario_id == 1
        assert sessao.resumo == "Terapia Cognitiva"

    def test_criar_sessao_service_simulado(self):
        class MockDB:
            def add(self, obj):
                self.obj = obj
            def commit(self):
                return True
            def refresh(self, obj):
                obj.id = 1
                return obj

        db = MockDB()
        sessao_data = Sessao(prontuario_id=1, resumo="Sessão de Avaliação")
        db.add(sessao_data)
        db.commit()
        db.refresh(sessao_data)
        assert sessao_data.id == 1
