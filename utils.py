from validacoes import validar_cpf, validar_entrada_vazia, validar_telefone
clientes = [] 
##esse vetor clientes é uma matriz, já que adiciono nele 4 informações [[nome][cpf][telefone][endereco]]
##isso no entanto fica assim: 
##[[nome][cpf][telefone][endereco]]
##[[nome][cpf][telefone][endereco]]
##[[nome][cpf][telefone][endereco]]

##verifica se a entrada nao está vazia, telefone e cpf, ai sim a função adiciona as informações na matriz
def adicionar_cliente(cpf, nome, telefone, endereco):
    if not validar_entrada_vazia(telefone,nome,endereco,cpf):
        print("Erro, entradas vázias")
        return
    if not validar_telefone(telefone=telefone):
        print("Erro, telefone errado")
        return
    if not validar_cpf(cpf=cpf):
        print("Erro, cpf inválido")
        return
    for cliente in clientes:
        if cliente[0] == cpf:
            print("Erro: CPF já cadastrado.")
            return
    clientes.append([cpf, nome, telefone, endereco])
    print("Cliente adicionado com sucesso.")


##busca pelo cpf e remove
def excluir_cliente(cpf):
    if not validar_cpf(cpf=cpf):
        print("Erro, cpf inválido")
        return
    for cliente in clientes:
        if cliente[0] == cpf:
            clientes.remove(cliente)
            print("Cliente removido com sucesso.")
            return
    print("Cliente não encontrado.")

def consultar_cliente(cpf):
    if not validar_cpf(cpf=cpf):
        print("Erro, cpf inválido")
        return
    for cliente in clientes:
        if cliente[0] == cpf:
            print("Cliente encontrado:")
            print(f"CPF: {cliente[0]}")
            print(f"Nome: {cliente[1]}")
            print(f"Telefone: {cliente[2]}")
            print(f"Endereço: {cliente[3]}")
            return
    print("Cliente não encontrado.")


##atualiza o cliente após verificar as entradas
def atualizar_cliente(cpf, novo_nome, novo_telefone, novo_endereco):
    if not validar_entrada_vazia(cpf, novo_endereco, novo_nome, novo_telefone):
        print("Erro, entradas vázias")
        return
    for cliente in clientes:
        if cliente[0] == cpf:
            cliente[1] = novo_nome or cliente[1]
            cliente[2] = novo_telefone or cliente[2]
            cliente[3] = novo_endereco or cliente[3]
            print("Dados do cliente atualizados com sucesso.")
            return
    print("Cliente não encontrado.")
