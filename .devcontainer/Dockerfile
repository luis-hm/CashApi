# Imagem base com Python
FROM python:3.12-slim

# Definir não interativo para evitar problemas no apt-get
ENV DEBIAN_FRONTEND=noninteractive

# Instalar dependências do sistema + ferramentas úteis
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    postgresql-client \
    curl \
    vim \
    netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

# Criar diretório de trabalho
WORKDIR /workspace

# Copiar e instalar dependências Python
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Script para aguardar o banco de dados
COPY .devcontainer/wait-for-db.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/wait-for-db.sh