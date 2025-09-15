# 💰 CashAPI – API de Controle Financeiro

A **CashAPI** é uma API RESTful para gerenciamento de finanças pessoais. Permite cadastrar usuários, categorias, transações (receitas/despesas) e gerar relatórios financeiros detalhados.

**Objetivo:** oferecer uma base sólida para um sistema de controle financeiro pessoal, que pode ser consumido por um frontend web ou mobile.

## 🛠️ Tecnologias Utilizadas

- **Python 3.12**
- **Django 5 + Django REST Framework**
- **PostgreSQL 15**
- **JWT Authentication** (SimpleJWT)
- **Docker + Dev Containers** (VSCode)
- **Documentação automática** (drf-spectacular → Swagger/ReDoc)

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos
- Docker instalado
- VSCode com extensão **Dev Containers**

### 2. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/cashapi.git
cd cashapi
```

### 3. Criar o arquivo `.env`
Crie o arquivo `.env` na raiz do projeto com:

```env
# Django
DEBUG=1
SECRET_KEY=super-secret-change-me
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

# Banco de dados
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=cashapi
SQL_USER=cashapi_user
SQL_PASSWORD=2oksiwt5
SQL_HOST=db
SQL_PORT=5432
```

### 4. Subir o ambiente com Dev Containers
No VSCode: **"Reopen in Container"**. Isso cria os containers (web e db) e instala as dependências.

### 5. Rodar as migrações
```bash
python manage.py migrate
```

### 6. Iniciar o servidor
```bash
python manage.py runserver 0.0.0.0:8000
```

A API ficará disponível em **http://localhost:8000/api/**

## 📚 Documentação Automática

- **Swagger** → http://localhost:8000/api/docs/
- **ReDoc** → http://localhost:8000/api/redoc/

## 🔐 Autenticação (JWT)

### Registrar usuário
**POST** `/api/auth/register/`

```json
{
  "email": "ana@example.com",
  "password": "123456"
}
```

### Obter token JWT
**POST** `/api/auth/token/`

```json
{
  "email": "ana@example.com", 
  "password": "123456"
}
```

O frontend deve enviar o token no cabeçalho:
```
Authorization: Bearer <access_token>
```

## 📂 Endpoints da API

### Categorias

- **GET** `/api/categories/` → lista categorias
- **POST** `/api/categories/` → cria categoria

**Exemplo de criação:**
```json
{
  "name": "Alimentação",
  "color": "#28A745"
}
```

### Transações

- **GET** `/api/transactions/` → lista transações
- **POST** `/api/transactions/` → cria transação

**Exemplo:**
```json
{
  "amount": 120.50,
  "type": "EXPENSE",
  "date": "2025-09-15",
  "category": "<id_da_categoria>"
}
```

### Relatórios

#### Saldo geral
**GET** `/api/reports/balance/`

**Resposta:**
```json
{
  "total_income": 5000,
  "total_expense": 3200,
  "balance": 1800
}
```

#### Resumo mensal
**GET** `/api/reports/monthly-summary/?year=2025&month=9`

**Resposta:**
```json
{
  "income": [
    {
      "category": "Salário",
      "total": 3500
    }
  ],
  "expense": [
    {
      "category": "Supermercado",
      "total": 120.50
    },
    {
      "category": "Academia",
      "total": 90.00
    }
  ]
}
```

#### Resumo geral
- **GET** `/api/reports/general-summary/?year=2025`
- **GET** `/api/reports/general-summary/?start_date=2025-01-01&end_date=2025-06-30`

## 📁 Estrutura do Projeto

```
cashapi/
├── apps/
│   ├── core/          → Utilidades (BaseModel, permissões, etc.)
│   ├── users/         → Registro e autenticação de usuários
│   ├── categories/    → Categorias de transações
│   ├── transactions/  → Receitas e despesas
│   └── reports/       → Relatórios financeiros
├── .devcontainer/     → Configuração Docker/DevContainers
├── cashapi/           → Configurações principais do Django
└── manage.py
```

## 🔄 Fluxo de Uso

1. **Usuário se cadastra** → `/api/auth/register/`
2. **Faz login e pega token JWT** → `/api/auth/token/`
3. **Cria categorias** → `/api/categories/` (Ex.: Alimentação, Transporte, Lazer)
4. **Registra transações** → `/api/transactions/` 
   - Uber: R$30 → Transporte
   - Supermercado: R$200 → Alimentação
5. **Consulta relatórios** →
   - `/api/reports/balance/` → saldo atual
   - `/api/reports/monthly-summary/?year=2025&month=9` → resumo do mês

## 🎯 Próximos Passos

- [ ] Implementar filtros avançados nas transações
- [ ] Adicionar suporte a múltiplas moedas
- [ ] Criar sistema de metas financeiras
- [ ] Implementar notificações por email
- [ ] Desenvolver dashboard web

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

---

⭐ Se este projeto te ajudou, deixe uma estrela no repositório!