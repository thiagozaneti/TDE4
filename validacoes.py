def validar_cpf(cpf):
    return len(cpf) == 11

def validar_telefone(telefone):
    return  8 <= len(telefone) <= 11

def validar_entrada_vazia(entrada_telefone, entrada_nome, entrada_endereco, entrada_cpf):
    return len(entrada_cpf) <= 0 and len(entrada_endereco) <= 0 and len(entrada_nome) <= 0 and len(entrada_telefone)
