def validar_cpf(cpf):
    return len(cpf) == 11

def validar_telefone(telefone):
    return  8 <= len(telefone) <= 11

def validar_entrada_vazia(entrada_telefone, entrada_nome, entrada_endereco, entrada_cpf):
    return all([entrada_cpf.strip(), entrada_endereco.strip(), entrada_nome.strip(), entrada_telefone.strip()])
