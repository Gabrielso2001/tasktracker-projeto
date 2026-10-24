# TaskTracker - Bootcamp II (Fase 3)
# Imagem leve e autossuficiente da aplicação CLI

# Base oficial do Python em versão "slim": só o essencial, imagem bem menor
FROM python:3.11-slim

# Pasta central de trabalho dentro do container
WORKDIR /app

# Envia a saída do print() direto para o terminal, sem atraso de buffer
ENV PYTHONUNBUFFERED=1

# Copia apenas o código-fonte da aplicação para dentro da imagem
COPY src/ /app/src/

# Comando executado quando o container inicia
CMD ["python", "src/main.py"]
