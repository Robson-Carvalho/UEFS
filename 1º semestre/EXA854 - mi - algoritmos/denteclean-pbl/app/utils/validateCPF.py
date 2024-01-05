def validateCPF(cpf):
    # Remove caracteres não numéricos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF possui 11 dígitos
    if len(cpf) != 11:
        print("\nValor inválido! O cpf precisa ter 11 dígitos.")
        return False

    # Calcula o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    digito1 = 11 - resto if resto >= 2 else 0

    # Verifica o primeiro dígito verificador
    if digito1 != int(cpf[9]):
        print("\nCPF inválido! Por favor! Forneça um CPF válido.")
        return False

    # Calcula o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    digito2 = 11 - resto if resto >= 2 else 0

    # Verifica o segundo dígito verificador
    if digito2 != int(cpf[10]):
        print("\nCPF inválido! Por favor! Forneça um CPF válido.")
        return False

    # Formata o CPF no formato padrão (###.###.###-##)
    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    return cpf_formatado
