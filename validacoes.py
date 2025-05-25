
##valida cpf
def validar_cpf(cpf):
    return len(cpf) == 11


##valida telefone
def validar_telefone(telefone):
    return  8 <= len(telefone) <= 11


##valida a entrada- remove espaços vazios
def validar_entrada_vazia(entrada_telefone, entrada_nome, entrada_endereco, entrada_cpf):
    return all([entrada_cpf.strip(), entrada_endereco.strip(), entrada_nome.strip(), entrada_telefone.strip()])
