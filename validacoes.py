def validar_cpf(cpf):
    if len(cpf) > 11:
        return cpf
    
def validar_entradas_vazias(entrada):
    if len(entrada) <= 0:
        print("entrada vazia")