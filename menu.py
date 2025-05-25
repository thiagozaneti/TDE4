def menu():
    while True:
        print("\n--- MENU CLIENTES ---")
        print("1 - Cadastrar cliente")
        print("2 - Consultar cliente")
        print("3 - Atualizar cliente")
        print("4 - Excluir cliente")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome: ")
            cpf = input("CPF (somente números): ")
            telefone = input("Telefone: ")
            endereco = input("Endereço: ")
            print("função de Create")

        elif opcao == '2':
            cpf = input("Digite o CPF do cliente: ")
            pass
            ##busca de cliente por cpf

        elif opcao == '3':
            cpf = input("Digite o CPF do cliente a ser atualizado: ")
            nome = input("Novo nome: ")
            telefone = input("Novo telefone: ")
            endereco = input("Novo endereço: ")
            print("Função de atualizar cliente")

        elif opcao == '4':
            cpf = input("Digite o CPF do cliente a ser excluído: ")
            print("função de excluir cliente")

        elif opcao == '5':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

