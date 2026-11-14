
# Imagem base do Python
FROM python:3.13-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Evita arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1

# Exibe logs imediatamente
ENV PYTHONUNBUFFERED=1

# Copia as dependências
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código da aplicação
COPY ./main.py .

# Copia o diretório do banco de dados
COPY ./database ./database
# Expõe a porta da API
EXPOSE 8000

# Inicializa o FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]