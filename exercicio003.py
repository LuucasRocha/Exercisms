""" 
Gerenciador de Lista de Tarefas (Nível Básico/Intermediário)
Objetivo: Criar um sistema simples para gerenciar uma lista de tarefas (To-Do List).
Tarefas:
Crie uma estrutura de dados (como uma lista ou array) para armazenar as tarefas.
Implemente um menu que permita ao usuário escolher entre as seguintes opções:
1. Adicionar Tarefa: O usuário deve inserir o nome de uma nova tarefa, que será adicionada à lista.
2. Visualizar Tarefas: O programa deve exibir todas as tarefas da lista, mostrando o número (índice) de cada uma.
3. Marcar Tarefa como Concluída (ou Remover): O usuário deve inserir o número da tarefa que deseja remover/marcar como concluída. O programa deve remover essa tarefa da lista.
4. Sair: Encerrar o programa.
Use um laço de repetição (como while) para manter o menu ativo até que o usuário escolha "Sair".
Dica de Lógica: Este exercício envolve o uso de estruturas de dados (listas/arrays), laços de repetição e estruturas condicionais (if/else ou switch/case) para controlar o fluxo do programa com base na escolha do usuário.
"""
tarefas = []

adicionar_tarefa = "1"
visualizar_tarefas = "2"
remover_tarefa = "3"
sair = "4"
opcao = ""

while opcao != sair:
    print("Menu:")
    print("1. Adicionar Tarefa")
    print("2. Visualizar Tarefas")
    print("3. Remover Tarefa")
    print("4. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == adicionar_tarefa:
        tarefa = input("Digite o nome da tarefa: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")

    elif opcao == visualizar_tarefas:
        print("Lista de Tarefas:")
        for i, t in enumerate(tarefas):
            print(f"{i + 1}. {t}")

    elif opcao == remover_tarefa:
        indice = int(input("Digite o número da tarefa que deseja remover: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefas.pop(indice)
            print("Tarefa removida com sucesso!")
        else:
            print("Tarefa não encontrada.")

    elif opcao == sair:
        print("Saindo do programa...")
    else:
        print("Opção inválida. Tente novamente.")
