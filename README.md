# TaskTracker

Sistema de gerenciamento de tarefas via linha de comando (CLI), desenvolvido em Python 3 como projeto individual da disciplina **Bootcamp II** (Análise e Desenvolvimento de Sistemas — UNICEUB).

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

- Python 3
- Git e GitHub

## Estrutura do repositório

```
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```

## Instalação e execução

Pré-requisito: Python 3 instalado.

```bash
git clone https://github.com/Gabrielso2001/tasktracker-projeto.git
cd tasktracker-projeto
```

No Windows:

```bash
python src\main.py
```

No Linux/macOS:

```bash
python3 src/main.py
```

## Fases do projeto

- **Fase 1** — Planejamento lógico (concluída)
- **Fase 2** — Repositório, versionamento e implementação em Python (atual)
- **Fase 3** — Empacotamento, Docker, testes e deploy

## Autor

Gabriel Silva — [@Gabrielso2001](https://github.com/Gabrielso2001)