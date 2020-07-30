import re

def remove_caracter(cpf):
    return re.sub(r'[^0-9]', '', cpf)