##arquivo para centralizar as funções do crud

clientes = []

def adicionar_cliente(cpf, nome, telefone, endereco):
    for i in clientes:
        if cpf == clientes[i]:
            clientes.append(cpf, nome,telefone, endereco )
    return print("Cliente Adicionado com sucesso")

def excluir_cliente(cpf):
    for i in clientes:
        if cpf == clientes[i]:
            clientes[i].remove
    return print("Cliente removido com sucesso")

def consultar_cliente(cpf):
    for cliente in clientes:
        if cliente[0] == cpf:
            print("Cliente encontrado:")
            print(f"CPF: {cliente[0]}")
            print(f"Telefone: {cliente[1]}")
            print(f"Endereço: {cliente[2]}")
            return
    print("Cliente não encontrado.")

def atualizar_cliente(cpf, novo_telefone, novo_endereco, novo_nome):
    for cliente in clientes:
        if cliente[0] == cpf:
            cliente[1] = novo_telefone
            cliente[2] = novo_endereco
            cliente[3] = novo_nome
            print("Dados do cliente atualizados com sucesso.")
            return
    print("Cliente não encontrado.")