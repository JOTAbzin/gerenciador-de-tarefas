def adicionar_tarefa(tarefas, nome_tarefa):  # Nome da função padronizado
    tarefa = {"tarefa": nome_tarefa, "concluida": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} adicionada com sucesso!")
    return


def ver_tarefas(tarefas):
    print("\nLista de tarefas:")
    for indice, tarefa in enumerate (tarefas , start=1):
        status = "✓" if tarefa["concluida"] else " "  
        nome_tarefa = tarefa["tarefa"] 
        print(f"{indice}. [{status}] {nome_tarefa}")
         #Indice da tarefa é o numero da tarefa na lista 

def atualizar_tarefa(tarefas, indice_tarefa, novo_nome):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas [indice_tarefa_ajustado  ] ["tarefa"] = novo_nome
        print(f"Tarefa {indice_tarefa} atualizada para {novo_nome}") 
    else:
        print(f"Não foi possível atualizar a tarefa Índice inválido.")
    return

def concluir_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    print(f"Tarefa {indice_tarefa} concluída com sucesso!")
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["concluida"] = True
        print(f"Tarefa {indice_tarefa} concluída com sucesso!")
    else:
        print(f"Não foi possível concluir a tarefa. Índice inválido.")


def remover_tarefa_concluida(tarefas):
    tarefas_concluidas = []
    for tarefa in tarefas:
        if tarefa["concluida"]:
            tarefas.remove(tarefa)
    print("Tarefas concluídas removidas com sucesso!")


tarefas = []

while True :
    print("\nMenu Gerenciador de Tarefas:")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Atualizar tarefa")
    print("4. Concluir tarefa")
    print("5. Remover tarefa concluida")
    print("6. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        nome_tarefa = input("Digite o nome da tarefa: ")
        adicionar_tarefa(tarefas, nome_tarefa)
    elif opcao == '2':
        ver_tarefas(tarefas)
    elif opcao == '3':
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite o índice da tarefa a ser atualizada: ")
        novo_nome = input("Digite o novo nome da tarefa: ")
        atualizar_tarefa(tarefas, indice_tarefa, novo_nome)
    elif opcao == '4':
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite o numero da tarefa a ser concluída: ")
        concluir_tarefa(tarefas, indice_tarefa)
    elif opcao == '5':
        remover_tarefa_concluida(tarefas)
        ver_tarefas(tarefas)



    elif opcao == '6':
        break
