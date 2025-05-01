# API de Prontuário Psicológico

Esta é uma API RESTful desenvolvida com FastAPI para registrar, organizar e consultar prontuários psicológicos de pacientes. A proposta é permitir que psicólogos e profissionais da área tenham uma base estruturada para integração com um aplicativo móvel ou sistema web.

---

## 🔧 Funcionalidades

- `POST /pacientes/`: Cadastra um novo paciente.
- `GET /pacientes/`: Lista todos os pacientes cadastrados.
- `POST /prontuarios/`: Registra um novo prontuário (sessão) para um paciente.
- `GET /prontuarios/`: Lista todos os prontuários cadastrados.

---

## 🗂️ Estrutura do Projeto

O projeto está organizado de forma modular para facilitar a manutenção e o crescimento futuro.

```
api-prontuariopsicologico/
├── app/
│   ├── __init__.py
│   ├── rotas/                # Rotas da API
│   │   ├── pacientes.py      # Endpoints de pacientes
│   │   └── prontuarios.py    # Endpoints de prontuários
│   ├── esquemas/             # Pydantic Schemas
│   │   ├── paciente.py
│   │   └── prontuario.py
│   └── principal.py          # Arquivo principal da aplicação
├── venv/                     # Ambiente virtual Python
├── requirements.txt          # Dependências do projeto
└── README.md                 # Documentação
```

---

## ▶️ Como Rodar a Aplicação

### ✅ Requisitos

- Python 3.8+
- FastAPI
- Uvicorn

### Passo a passo

Clone o repositório:

```bash
git clone https://github.com/wagnersantan/api-prontuariopsicologico.git
cd api-prontuariopsicologico
```

Crie um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o servidor localmente:

```bash
uvicorn app.principal:app --reload
```

A API estará disponível em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📑 Testando a API

Use a interface interativa automática gerada pelo FastAPI:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🚧 Próximos Passos

- Integração com banco de dados MongoDB Atlas 🌍
- Implementar autenticação de usuários (JWT)
- Relatórios e filtros de sessões por paciente
- Upload de arquivos (como anotações ou registros de voz)

---

## 🤝 Contribuição

Sinta-se à vontade para colaborar:

1. Faça um fork do projeto
2. Crie uma branch (`git checkout -b minha-melhoria`)
3. Commit suas alterações (`git commit -m 'feat: adicionei nova funcionalidade'`)
4. Dê um push (`git push origin minha-melhoria`)
5. Abra um Pull Request

---

## ⚖️ Licença

Distribuído sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Desenvolvido por **Wagner Santana**.
