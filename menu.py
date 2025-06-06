from utils import adicionar_cliente, atualizar_cliente, consultar_cliente, excluir_cliente, clientes


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
            nome_add = input("Nome: ")
            cpf_add = input("CPF (somente números): ")
            telefone_add = input("Telefone: ")
            endereco_add = input("Endereço: ")
            adicionar_cliente(cpf=cpf_add, nome = nome_add, telefone= telefone_add, endereco= endereco_add)
            for i in clientes:
                print(i)
            

        elif opcao == '2':
            cpf = input("Digite o CPF do cliente: ")
            consultar_cliente(cpf=cpf)

        elif opcao == '3':
            cpf = input("Digite o CPF do cliente a ser atualizado: ")
            nome = input("Novo nome: ")
            telefone = input("Novo telefone: ")
            endereco = input("Novo endereço: ")
            atualizar_cliente(nome, telefone, cpf, endereco)

        elif opcao == '4':
            cpf = input("Digite o CPF do cliente a ser excluído: ")
            excluir_cliente(cpf=cpf)

        elif opcao == '5':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")

