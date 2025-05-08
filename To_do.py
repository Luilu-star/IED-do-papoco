tarefas = []            # Lista principal de tarefas
historico = []          # Pilha para desfazer tarefas
fila_execucao = []      # Fila para executar tarefas

def adicionar_tarefa(tarefa): # Adiciona uma tarefa à lista principal, pilha e fila
    tarefas.append(tarefa) # Adiciona à lista principal
    historico.append(tarefa) # Adiciona à pilha para desfazer
    fila_execucao.append(tarefa) # Adiciona à fila para marcar como atendida
    print(f"Tarefa '{tarefa}' adicionada!\n") # Retorna mensagem de confirmação da adição da tarefa à lista

def desfazer_ultima_tarefa(): # Desfaz a última tarefa adicionada
    if historico: # Verifica se há tarefas na pilha
        ultima = historico.pop() # Remove a última tarefa da pilha
        tarefas.remove(ultima) # Remove a tarefa da lista principal
        fila_execucao.remove(ultima) # Remove a tarefa da fila de execução
        print(f"Tarefa '{ultima}' desfeita!\n") # Retorna mensagem de confirmação da remoção da tarefa
    else:
        print("Nenhuma tarefa para desfazer.\n") # Retorna mensagem de erro caso não haja tarefas na pilha

def atender_tarefa(): # Marca a tarefa da fila de execução como concluída
    if fila_execucao: # Verifica se há tarefas na fila
        feita = fila_execucao.pop(0) # Remove a primeira tarefa da fila
        tarefas.remove(feita) # Remove a tarefa da lista principal
        print(f"Tarefa '{feita}' atendida!\n") # Retorna mensagem de confirmação da remoção da tarefa
    else:
        print("Nenhuma tarefa para atender.\n") # Retorna mensagem de erro caso não haja tarefas na fila

def mostrar_tarefas(): # Mostra todas as tarefas na lista principal
    print("\n📋 Lista de Tarefas:") # Retorna uma mensagem/cabeçalho da lista de tarefas
    for i, t in enumerate(tarefas): # Percorre a lista de tarefas
        print(f"{i + 1}. {t}") # Retorna a tarefa com seu respectivo índice
    print() # Espaçamento entre as tarefas

def montar_arquivo(): # Monta um arquivo com as tarefas
    nome_arquivo = "todo_list.txt" # Nome do arquivo a ser criado

    if tarefas: # Verifica se há tarefas na lista principal
        with open(nome_arquivo, "w") as file: # Abre o arquivo para escrita
            for item in tarefas: # Percorre a lista de tarefas
                file.write(item + "\n") # Escreve cada tarefa no arquivo

        print(f'Tarefas salvas no arquivo {nome_arquivo}!') # Retorna mensagem de confirmação da criação do arquivo


while True:  # Inicia um loop infinito para o menu interativo
    print("1. Adicionar Tarefa")  # Exibe a opção de adicionar uma tarefa
    print("2. Desfazer Última Tarefa")  # Exibe a opção de desfazer a última tarefa
    print("3. Atender Tarefa (modo fila)")  # Exibe a opção de marcar uma tarefa como concluída no modo fila
    print("4. Mostrar Tarefas")  # Exibe a opção de mostrar todas as tarefas
    print("5. Sair")  # Exibe a opção de sair do programa

    opcao = input("Escolha uma opção: ")  # Solicita ao usuário que escolha uma opção do menu

    if opcao == '1':  # Verifica se o usuário escolheu a opção 1
        tarefa_text = input("Digite a tarefa: ")  # Solicita o texto da tarefa
        dia = input("Digite o dia (DD): ") # Solicita o dia final da tarefa
        mes = input("Digite o mês (MM): ") # Solicita o mês final da tarefa
        ano = input("Digite o ano (AA): ") # Solicita o ano final da tarefa
        data_conc = f'{dia}/{mes}/{ano}'  # Formata a data no formato DD/MM/AA

        # Adiciona a tarefa com as informações fornecidas pelo usuário
        adicionar_tarefa(f'{tarefa_text}, Data final: [{data_conc}]')
    elif opcao == '2':  # Verifica se o usuário escolheu a opção 2
        desfazer_ultima_tarefa()  # Chama a função para desfazer a última tarefa
    elif opcao == '3':  # Verifica se o usuário escolheu a opção 3
        atender_tarefa()  # Chama a função para atender a próxima tarefa na fila
    elif opcao == '4':  # Verifica se o usuário escolheu a opção 4
        mostrar_tarefas()  # Chama a função para exibir todas as tarefas
    elif opcao == '5':  # Verifica se o usuário escolheu a opção 5
        montar_arquivo()  # Salva as tarefas em um arquivo antes de sair
        print("Saindo do programa...")  # Exibe uma mensagem de saída
        break  # Encerra o loop e o programa
    else:
        print("Opção inválida!\n")  # Exibe uma mensagem de erro caso a opção escolhida não seja válida
