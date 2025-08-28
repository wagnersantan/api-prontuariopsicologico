# API de Prontuário Psicológico

API RESTful desenvolvida com **FastAPI** para gerenciar prontuários psicológicos: pacientes, sessões, evoluções, documentos e usuários (com autenticação JWT).

---

## ✨ Principais Recursos

* **Pacientes**: CRUD completo.
* **Prontuários** (registros de atendimento): CRUD completo.
* **Sessões**: criação e listagem.
* **Evoluções**: criação e listagem.
* **Documentos**: upload/registro e listagem.
* **Usuários & Autenticação (JWT)**: criação de usuário, login e rota protegida `me`.

> **Versão da API**: v1
> **Prefixo base**: `/api/v1`

---

## 🗂️ Estrutura do Projeto

```
api-prontuariopsicologico/
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── routes/
│   │           ├── alertas/
│   │           ├── auth/
│   │           ├── documentos/
│   │           ├── evolucoes/
│   │           ├── pacientes/
│   │           ├── prontuarios/
│   │           ├── sessoes/
│   │           └── usuarios/
│   └── main.py
├── core/
│   ├── config.py
│   └── database.py
├── models/
├── repositories/
├── schemas/
├── services/
├── testes/
├── utils/
├── requirements.txt
├── database.db
├── README.md
└── LICENSE
```

---

## ▶️ Como Rodar Localmente

### Pré‑requisitos

* Python **3.12+** (ou 3.10+/3.11+ se preferir)
* Pip e venv

### Passo a passo

```bash
# 1) Clonar o repositório
git clone https://github.com/wagnersantan/api-prontuariopsicologico.git
cd api-prontuariopsicologico

# 2) Criar e ativar o ambiente virtual
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3) Instalar dependências
pip install -r requirements.txt

# 4) Executar o servidor
uvicorn app.main:app --reload
```

A API ficará disponível em: `http://127.0.0.1:8000`

### Documentação automática

* **Swagger UI**: `http://127.0.0.1:8000/docs`
* **ReDoc**: `http://127.0.0.1:8000/redoc`

> Se você preferir outro host/porta: `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`.

---

## 🔐 Configuração (env)

As configurações básicas ficam em `core/config.py` e o banco em `core/database.py`. Por padrão, usa‑se **SQLite** em `database.db`.

Exemplo de `.env` (opcional, se já estiver embutido no `config.py`):

```
# Exemplo
DATABASE_URL=sqlite:///./database.db
JWT_SECRET=troque-por-um-segredo-forte
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

## 📚 Endpoints (v1)

> Os exemplos abaixo assumem o **prefixo base** `/api/v1`.

### Pacientes

* `POST /pacientes/` – Cadastrar paciente
* `GET /pacientes/` – Listar pacientes
* `GET /pacientes/{id}` – Obter paciente por ID
* `PUT /pacientes/{id}` – Atualizar paciente
* `DELETE /pacientes/{id}` – Remover paciente

**Exemplo de request (POST /pacientes/):**

```json
{
  "nome": "Wagner Santana",
  "cpf": "123.456.789-00",
  "rg": "MG-12.345.678",
  "data_nascimento": "1985-08-27",
  "genero": "Masculino",
  "email": "wagner.santana@example.com",
  "telefone": "(31) 99999-0000",
  "endereco": "Rua Exemplo, 123, Belo Horizonte, MG",
  "contato_emergencia": "Maria Santana - (31) 98888-0000",
  "plano_saude": "Unimed",
  "numero_carteirinha": "000123456",
  "historico_atendimentos": [],
  "diagnosticos": ["Ansiedade leve"],
  "medicamentos": [],
  "observacoes": "Paciente relata ansiedade leve."
}
```

### Prontuários

* `POST /prontuarios/` – Criar prontuário (sessão) para paciente
* `GET /prontuarios/` – Listar prontuários
* `GET /prontuarios/{id}` – Obter prontuário por ID
* `PUT /prontuarios/{id}` – Atualizar prontuário
* `DELETE /prontuarios/{id}` – Remover prontuário

### Sessões

* `POST /sessoes/` – Criar sessão
* `GET /sessoes/` – Listar sessões
* `GET /sessoes/{id}` – Obter sessão por ID

### Evoluções

* `POST /evolucoes/` – Registrar evolução
* `GET /evolucoes/` – Listar evoluções
* `GET /evolucoes/{id}` – Obter evolução por ID

### Documentos

* `POST /documentos/` – Adicionar documento
* `GET /documentos/` – Listar documentos
* `GET /documentos/{id}` – Obter documento por ID

### Usuários & Auth

* `POST /usuarios/` – Criar novo usuário (ex.: psicólogo/admin)
* `POST /auth/login` – Login (retorna **JWT**)
* `GET /usuarios/me` – Dados do usuário autenticado (**Bearer Token**)

---

## 🧪 Exemplos rápidos (cURL)

```bash
# Criar paciente
curl -X POST http://127.0.0.1:8000/api/v1/pacientes/ \
  -H "Content-Type: application/json" \
  -d '{
    "nome":"Wagner Santana",
    "cpf":"123.456.789-00",
    "rg":"MG-12.345.678",
    "data_nascimento":"1985-08-27",
    "genero":"Masculino",
    "email":"wagner.santana@example.com",
    "telefone":"(31) 99999-0000",
    "endereco":"Rua Exemplo, 123, BH",
    "contato_emergencia":"Maria Santana - (31) 98888-0000",
    "plano_saude":"Unimed",
    "numero_carteirinha":"000123456",
    "historico_atendimentos":[],
    "diagnosticos":["Ansiedade leve"],
    "medicamentos":[],
    "observacoes":"Paciente relata ansiedade leve."
  }'

# Listar pacientes
curl http://127.0.0.1:8000/api/v1/pacientes/

# Login (exemplo)
curl -X POST http://127.0.0.1:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"username":"demo","password":"demo"}'

# Rota protegida (substitua TOKEN pelo JWT)
curl http://127.0.0.1:8000/api/v1/usuarios/me \
  -H "Authorization: Bearer TOKEN"
```

---

## ✅ Testes

Se houver testes automatizados (pasta `testes/`), execute:

```bash
pytest -q
```

> Garanta que o ambiente esteja ativo e dependências instaladas.

---


## 🤝 Contribuição

1. Faça um **fork**
2. Crie uma branch: `git checkout -b minha-melhoria`
3. Commit: `git commit -m 'feat: nova funcionalidade'`
4. Push: `git push origin minha-melhoria`
5. Abra um **Pull Request**

---

## ⚖️ Licença

Distribuído sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE).

---

Desenvolvido por **Wagner Santana**.
