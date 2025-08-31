# 📚 Documentação de Endpoints – API de Prontuário Psicológico

Esta documentação apresenta todos os endpoints disponíveis na API, com exemplos de requests e responses.  
Você pode testar todos os endpoints de forma interativa usando o Swagger UI:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧑‍🤝‍🧑 Pacientes

### 1. Cadastrar novo paciente
- **Endpoint:** `POST /pacientes/`
- **Request Body:**
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


{
  "id": "uuid-gerado",
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

2. Listar todos os pacientes

Endpoint: GET /pacientes/

Response:
[
  {
    "id": "uuid-do-paciente",
    "nome": "Wagner Santana",
    "cpf": "123.456.789-00",
    "email": "wagner.santana@example.com"
  },
  {
    "id": "uuid-do-paciente-2",
    "nome": "Maria Silva",
    "cpf": "987.654.321-00",
    "email": "maria.silva@example.com"
  }
]

3. Consultar paciente específico

Endpoint: GET /pacientes/{id}

4. Atualizar paciente

Endpoint: PUT /pacientes/{id}

5. Remover paciente

Endpoint: DELETE /pacientes/{id}

📄 Prontuários
1. Registrar novo prontuário

Endpoint: POST /prontuarios/

Request Body:

{
  "paciente_id": "uuid-do-paciente",
  "sessao_id": "uuid-da-sessao",
  "descricao": "Sessão realizada com foco em ansiedade",
  "data": "2025-08-27"
}

{
  "id": "uuid-prontuario",
  "paciente_id": "uuid-do-paciente",
  "sessao_id": "uuid-da-sessao",
  "descricao": "Sessão realizada com foco em ansiedade",
  "data": "2025-08-27"
}

2. Listar todos os prontuários

Endpoint: GET /prontuarios/

3. Consultar, atualizar e remover prontuário

Endpoints: GET /prontuarios/{id}, PUT /prontuarios/{id}, DELETE /prontuarios/{id}

📝 Sessões
1. Criar nova sessão

Endpoint: POST /sessoes/

2. Listar sessões

Endpoint: GET /sessoes/

3. Consultar sessão específica

Endpoint: GET /sessoes/{id}

📈 Evoluções
1. Registrar evolução

Endpoint: POST /evolucoes/

2. Listar evoluções

Endpoint: GET /evolucoes/

3. Consultar evolução específica

Endpoint: GET /evolucoes/{id}

📁 Documentos
1. Adicionar documento

Endpoint: POST /documentos/

2. Listar documentos

Endpoint: GET /documentos/

3. Consultar documento específico

Endpoint: GET /documentos/{id}

🔑 Usuários / Autenticação
1. Criar usuário

Endpoint: POST /usuarios/

2. Login

Endpoint: POST /auth/login

3. Consultar dados do usuário autenticado

Endpoint: GET /usuarios/me

Todos os endpoints podem ser testados interativamente no Swagger UI: http://127.0.0.1:8000/docs