"""
TaskTracker - Sistema de Gerenciamento de Tarefas (CLI)
Bootcamp II - Fase 2 (Entrega Intermediária)
Autor: Gabriel Silva
"""


def cadastrar_tarefa(tarefas):
    """Coleta os dados e adiciona a nova tarefa à lista."""
    print("\n--- CADASTRAR NOVA TAREFA ---")
    titulo = input("Título: ").strip()
    descricao = input("Descrição: ").strip()
    prioridade = input("Prioridade (Alta / Média / Baixa): ").strip()
    data_limite = input("Data limite (DD/MM/AAAA): ").strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
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
    main()
