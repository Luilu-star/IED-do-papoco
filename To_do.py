tarefas = []            # Cria uma lista vazia chamada 'tarefas' para armazenar as tarefas
historico = []          # Cria uma lista vazia chamada 'historico' para armazenar o histórico de tarefas (pilha)
fila_execucao = []      # Cria uma lista vazia chamada 'fila_execucao' para armazenar as tarefas em uma fila (FIFO)

def adicionar_tarefa(tarefa):  # Define uma função para adicionar uma tarefa às listas
    tarefas.append(tarefa)  # O método append adiciona o valor 'tarefa' ao final da lista 'tarefas'
    historico.append(tarefa)  # O método append adiciona o valor 'tarefa' ao final da lista 'historico'
    fila_execucao.append(tarefa)  # O método append adiciona o valor 'tarefa' ao final da lista 'fila_execucao'
    print(f"Tarefa '{tarefa}' adicionada!\n")  # Exibe uma mensagem formatada com a tarefa adicionada

def desfazer_ultima_tarefa():  # Define uma função para desfazer a última tarefa adicionada
    if historico:  # Verifica se a lista 'historico' não está vazia
        ultima = historico.pop()  # O método pop remove e retorna o último elemento da lista 'historico'
        tarefas.remove(ultima)  # O método remove exclui o valor 'ultima' da lista 'tarefas'
        fila_execucao.remove(ultima)  # O método remove exclui o valor 'ultima' da lista 'fila_execucao'
        print(f"Tarefa '{ultima}' desfeita!\n")  # Exibe uma mensagem formatada com a tarefa desfeita
    else:
        print("Nenhuma tarefa para desfazer.\n")  # Exibe uma mensagem caso não haja tarefas no histórico

def atender_tarefa():  # Define uma função para atender a próxima tarefa na fila
    if fila_execucao:  # Verifica se a lista 'fila_execucao' não está vazia
        feita = fila_execucao.pop(0)  # O método pop(0) remove e retorna o primeiro elemento da lista 'fila_execucao'
        tarefas.remove(feita)  # O método remove exclui o valor 'feita' da lista 'tarefas'
        print(f"Tarefa '{feita}' atendida!\n")  # Exibe uma mensagem formatada com a tarefa atendida
    else:
        print("Nenhuma tarefa para atender.\n")  # Exibe uma mensagem caso não haja tarefas na fila

def mostrar_tarefas():  # Define uma função para exibir todas as tarefas na lista principal
    print("\n📋 Lista de Tarefas:")  # Exibe um cabeçalho para a lista de tarefas
    for i, t in enumerate(tarefas):  # O enumerate retorna o índice e o valor de cada elemento da lista 'tarefas'
        print(f"{i + 1}. {t}")  # Exibe o índice (começando em 1) e o valor de cada tarefa
    print()  # Adiciona uma linha em branco para espaçamento

def montar_arquivo():  # Define uma função para salvar as tarefas em um arquivo de texto
    nome_arquivo = "todo_list.txt"  # Define o nome do arquivo onde as tarefas serão salvas

    if tarefas:  # Verifica se a lista 'tarefas' não está vazia
        with open(nome_arquivo, "w") as file:  # O open abre o arquivo no modo de escrita ("w") e o with garante o fechamento automático
            for item in tarefas:  # Itera sobre cada elemento da lista 'tarefas'
                file.write(item + "\n")  # O método write escreve o valor 'item' no arquivo, seguido de uma nova linha
        print(f'Tarefas salvas no arquivo {nome_arquivo}!')  # Exibe uma mensagem confirmando a criação do arquivo

while True:  # Inicia um loop infinito que mantém o programa em execução até que o usuário escolha sair
    print("\nMenu de Opções:")  # Exibe o menu de opções para o usuário
    print("1. Adicionar Tarefa")  # Mostra a opção para adicionar uma nova tarefa
    print("2. Desfazer Última Tarefa")  # Mostra a opção para desfazer a última tarefa adicionada
    print("3. Atender Tarefa (modo fila)")  # Mostra a opção para atender a próxima tarefa na fila
    print("4. Mostrar Tarefas")  # Mostra a opção para exibir todas as tarefas pendentes
    print("5. Salvar Tarefas em Arquivo")  # Mostra a opção para salvar as tarefas em um arquivo de texto
    print("6. Sair")  # Mostra a opção para encerrar o programa

    opcao = input("Escolha uma opção: ")  # Solicita ao usuário que insira uma opção do menu e armazena como string

    if opcao == '1':  # Verifica se a opção escolhida pelo usuário é '1'
        tarefa_text = input("Digite a tarefa: ")  # Solicita ao usuário que insira o texto da tarefa e armazena na variável
        dia = input("Digite o dia (dd): ")  # Solicita ao usuário que insira o dia e armazena na variável
        mes = input("Digite o mês (mm): ")  # Solicita ao usuário que insira o mês e armazena na variável
        ano = input("Digite o ano (yy): ")  # Solicita ao usuário que insira o ano e armazena na variável
        data_conc = f'{ano}-{mes}-{dia}'  # Formata a data de vencimento no formato 'yy-mm-dd' e armazena na variável

        # Chama a função `adicionar_tarefa` para adicionar a tarefa formatada com as datas à lista de tarefas
        adicionar_tarefa(f'{tarefa_text}, Data final: [{data_conc}]')
    elif opcao == '2':  # Verifica se a opção escolhida pelo usuário é '2'
        desfazer_ultima_tarefa()  # Chama a função `desfazer_ultima_tarefa` para remover a última tarefa adicionada
    elif opcao == '3':  # Verifica se a opção escolhida pelo usuário é '3'
        atender_tarefa()  # Chama a função `atender_tarefa` para processar a próxima tarefa na fila
    elif opcao == '4':  # Verifica se a opção escolhida pelo usuário é '4'
        mostrar_tarefas()  # Chama a função `mostrar_tarefas` para exibir todas as tarefas pendentes
    elif opcao == '5':  # Verifica se a opção escolhida pelo usuário é '5'
        montar_arquivo()  # Chama a função `montar_arquivo` para salvar as tarefas em um arquivo de texto
        print("Tarefas salvas com sucesso!")  # Exibe uma mensagem confirmando que as tarefas foram salvas
    elif opcao == '6':  # Verifica se a opção escolhida pelo usuário é '6'
        print("Saindo do programa...")  # Exibe uma mensagem indicando que o programa será encerrado
        break  # Encerra o loop infinito, finalizando o programa
    else:  # Caso o usuário insira uma opção que não está no menu
        print("Opção inválida! Tente novamente.\n")  # Exibe uma mensagem informando que a opção é inválida
