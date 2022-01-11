import re

from validate_docbr import CPF

def cpf_valido(num_cpf):
    cpf = CPF()
    return cpf.validate(num_cpf)


def nome_valido(nome):
    return nome.isalpha()


def rg_valido(num_rg):
    return len(num_rg) == 9


def celular_valido(num_celular):
    """Verifica se o celular é valido (00 00000-0000)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, num_celular)
    return resposta
