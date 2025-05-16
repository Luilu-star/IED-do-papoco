usuarios = []
transporteInfo = {}
pessoa = {}

def mostrarusu():
    for item in usuarios:
        i = 0
        i = i + 1
        print(f"{i}.   {usuarios[i - 1]}")


while True:
    print('---------------------------')
    print('-   ⚙️     Menu     ⚙️    -')
    print()
    print('   1. Adicionar usuário    ')
    print('   2. Deletar usuário      ')
    print('   3. Ver usuários         ')
    print('   4. Sair do programa     ')
    print('---------------------------')

    option = int(input("Selecione uma opção acima: "))

    match option:
        case 1:
            pessoa["nome"] = input("Insira seu nome abaixo: ").capitalize()
            pessoa["cidade"] = input("Insira sua cidade abaixo: ").capitalize()
            pessoa["possuiTransporte"] = input("Você possui transporte? (Sim / Não)").lower()

            if pessoa["possuiTransporte"] == "sim":
                transporteInfo["Tipo"] = input("Qual o tipo de transporte? ").capitalize()
                transporteInfo["Propriedade"] = input("Você possui ou aluga? ").capitalize()

                pessoa["tansporteInfo"] = transporteInfo
            

                usuarios.append(f'Nome: {pessoa["nome"]}, Cidade: {pessoa["cidade"]}, Tem transporte: {pessoa["possuiTransporte"]}, Sobre o transporte: {pessoa["tansporteInfo"]}')
                print("Informações de usuário salvas com sucesso!")
            else:
                usuarios.append(f'Nome: {pessoa["nome"]}, Cidade: {pessoa["cidade"]}, Tem transporte: {pessoa["possuiTransporte"]}')

                print("Informações de usuário salvas com sucesso!")
            
        
        case 2:

            mostrarusu()

            index = int(input("qual dos acima deseja deletar?"))
            usuarios.pop(index - 1)

            
            print("Processo concluído!")
            
            
        case 3:
            mostrarusu()

        case 4:
            print("Saindo...")
            break

        case _:
            print("Opção inválida")



