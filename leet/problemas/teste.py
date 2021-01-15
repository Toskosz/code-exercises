from email_validator import


def verifica_digitos_verificadores_cpf(cpf):
    cpf_temp = cpf[::-1]
    cpf_temp = cpf_temp[2:]
    cpf_temp = [int(x) for x in cpf_temp]
    v1 = 0
    v2 = 0
    for i in range(0, 9):
        v1 = v1 + cpf_temp[i] * (9 - (i % 10))
        v2 = v2 + cpf_temp[i] * (9 - ((i+1) % 10))
    v1 = ( v1 % 11) % 10
    v2 = v2 + v1 * 9
    v2 = (v2 % 11) % 10
    if str(v1) != cpf[-2] or str(v2) != cpf[-1]:
        return 1
    else:
        return 0


def email_invalido(email):
    # nao pode ter jogo da velha
    if '#' in email:
        return 1
    # nao pode ter caracteres especiais seguidos
    if
        return 1
    # nao pode começar com caracetere especial
    # dominio valido

