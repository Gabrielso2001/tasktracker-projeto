"""
TaskTracker - Sistema de Gerenciamento de Tarefas (CLI)
Bootcamp II - Fase 2 (Entrega Intermediária)
Autor: Gabriel Silva
"""

PRIORIDADES_VALIDAS = {
    "alta": "Alta",
    "média": "Média",
    "media": "Média",
    "baixa": "Baixa",
}


# ---------------------------------------------------------------------------
# Funções de validação (regras de negócio)
# ---------------------------------------------------------------------------

def ler_titulo():
    """Solicita o título até que um valor não vazio seja informado."""
    while True:
        titulo = input("Título: ").strip()
        if titulo:
            return titulo
        print("[ERRO] O título é obrigatório e não pode ficar vazio. Tente novamente.")


def ler_prioridade():
    """Aceita apenas Alta, Média (ou Media) e Baixa, sem diferenciar maiúsculas."""
    while True:
        entrada = input("Prioridade (Alta / Média / Baixa): ").strip().lower()
        if entrada in PRIORIDADES_VALIDAS:
            return PRIORIDADES_VALIDAS[entrada]
        print("[ERRO] Prioridade inválida. Digite apenas: Alta, Média ou Baixa.")


# ---------------------------------------------------------------------------
# Funcionalidades
# ---------------------------------------------------------------------------

def cadastrar_tarefa(tarefas):
    """Coleta os dados, valida e adiciona a nova tarefa à lista."""
    print("\n--- CADASTRAR NOVA TAREFA ---")
    titulo = ler_titulo()
    descricao = input("Descrição: ").strip()
    prioridade = ler_prioridade()
    data_limite = input("Data limite (DD/MM/AAAA): ").strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",  # definido automaticamente
    }
    tarefas.append(tarefa)
    print(f"\n[OK] Tarefa '{titulo}' cadastrada com sucesso!")


def listar_tarefas(tarefas):
    """Exibe todas as tarefas ou avisa que a lista está vazia."""
    print("\n--- TAREFAS CADASTRADAS ---")
    if not tarefas:
        print("Nenhuma tarefa cadastrada no momento.")
        return

    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa #{numero}")
        print(f"  Título:      {tarefa['titulo']}")
        print(f"  Descrição:   {tarefa['descricao'] or '(sem descrição)'}")
        print(f"  Prioridade:  {tarefa['prioridade']}")
        print(f"  Data limite: {tarefa['data_limite'] or '(não informada)'}")
        print(f"  Status:      {tarefa['status']}")
    print(f"\nTotal: {len(tarefas)} tarefa(s).")


def exibir_menu():
    print("\n==============================")
    print("        TASKTRACKER")
    print("==============================")
    print("1. Cadastrar nova tarefa")
    print("2. Visualizar tarefas cadastradas")
    print("3. Sair da aplicação")


# ---------------------------------------------------------------------------
# Loop principal
# ---------------------------------------------------------------------------

def main():
    tarefas = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            print("\nEncerrando o TaskTracker. Até logo!")
            break
        else:
            print("[ERRO] Opção inválida. Digite 1, 2 ou 3.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n\nAplicação encerrada pelo usuário.")