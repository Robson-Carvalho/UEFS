def validateCPF(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        print("\nValor inválido! O cpf precisa ter 11 dígitos.")
        return False

    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    digito1 = 11 - resto if resto >= 2 else 0

    if digito1 != int(cpf[9]):
        print("\nCPF inválido! Por favor! Forneça um CPF válido.")
        return False

    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    digito2 = 11 - resto if resto >= 2 else 0

    if digito2 != int(cpf[10]):
        print("\nCPF inválido! Por favor! Forneça um CPF válido.")
        return False

    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    return cpf_formatado

"""
Autor: Robson Carvalho de Souza

Componente Curricular: EXA 854-MI-Algoritmos

Concluido em: 08/02/2024

Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
"""
