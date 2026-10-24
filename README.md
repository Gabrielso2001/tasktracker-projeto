# TaskTracker

Sistema de gerenciamento de tarefas via linha de comando (CLI), desenvolvido em Python 3 como projeto individual da disciplina **Bootcamp II** (Análise e Desenvolvimento de Sistemas — UNICEUB).

Na Fase 3 a aplicação foi **conteinerizada com Docker**, garantindo que rode de forma idêntica em qualquer máquina, sem precisar instalar Python.

## Descrição funcional

O TaskTracker permite cadastrar e visualizar tarefas pelo terminal. Cada tarefa possui:

| Campo | Regra |
|---|---|
| Título | Obrigatório; entradas vazias ou só com espaços são rejeitadas |
| Descrição | Texto livre |
| Prioridade | Apenas `Alta`, `Média` (ou `Media`) ou `Baixa` |
| Data limite | Formato livre ou DD/MM/AAAA |
| Status | Definido automaticamente como `Pendente` |

Menu da aplicação:

1. Cadastrar nova tarefa
2. Visualizar tarefas cadastradas
3. Sair da aplicação

## Tecnologias utilizadas

- Python 3.11
- Docker e Docker Compose
- Git e GitHub

## Estrutura do repositório

```
tasktracker-projeto/
├── .gitignore
├── .dockerignore
├── docs/
│   └── planejamento_logico.pdf   # Fase 1 — planejamento lógico
├── src/
│   └── main.py                   # Fase 2 — código Python da CLI
├── Dockerfile                    # Fase 3 — receita da imagem
├── docker-compose.yml            # Fase 3 — orquestração interativa
└── README.md
```

## Executando com Docker (recomendado)

Pré-requisito: [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado e aberto.

```bash
git clone https://github.com/Gabrielso2001/tasktracker-projeto.git
cd tasktracker-projeto
```

### 1. Como construir a imagem

```bash
docker build -t tasktracker-app .
```

### 2. Como rodar o container em modo isolado

```bash
docker run -it --rm tasktracker-app
```

> `-i` mantém a entrada aberta, `-t` cria o terminal interativo e `--rm` remove o container ao sair.

### 3. Como rodar via orquestração (recomendado)

```bash
docker compose run --rm tasktracker
```

> O `docker-compose.yml` já define `stdin_open: true` e `tty: true`, necessários para o `input()` da CLI funcionar dentro do container. Se a imagem ainda não existir, o Compose faz o build automaticamente.

## Decisões técnicas

**Dockerfile**

| Instrução | Motivo |
|---|---|
| `FROM python:3.11-slim` | Imagem base oficial e enxuta, com apenas o necessário para rodar Python |
| `WORKDIR /app` | Define a pasta de trabalho dentro do container |
| `ENV PYTHONUNBUFFERED=1` | Mostra a saída do `print()` imediatamente no terminal, sem buffer |
| `COPY src/ /app/src/` | Copia só o código-fonte para a imagem |
| `CMD ["python", "src/main.py"]` | Inicia a aplicação quando o container sobe |

**docker-compose.yml**

| Configuração | Motivo |
|---|---|
| `build: .` | Constrói a imagem a partir do Dockerfile da raiz |
| `stdin_open: true` | Mantém o canal de entrada aberto (equivale ao `-i`) |
| `tty: true` | Aloca um terminal virtual (equivale ao `-t`) |

O `.dockerignore` evita copiar para o contexto de build arquivos desnecessários como `.git` e `docs/`.

## Executando sem Docker (alternativa)

Pré-requisito: Python 3 instalado.

```bash
python src/main.py
```

## Fases do projeto

- **Fase 1** — Planejamento lógico e pseudocódigo (concluída)
- **Fase 2** — Repositório, versionamento e implementação em Python (concluída)
- **Fase 3** — Conteinerização, orquestração e deploy com Docker (concluída)

## Autor

Gabriel Silva de Oliveira — [@Gabrielso2001](https://github.com/Gabrielso2001)
