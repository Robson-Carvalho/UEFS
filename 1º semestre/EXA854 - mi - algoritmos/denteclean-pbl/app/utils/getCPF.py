from utils.validateCPF import validateCPF

def getCPF():
    cpf = False
    while cpf == False:
        cpf = input("\nDigite o cpf do paciente: ")
        cpf = validateCPF(cpf)

        if cpf == False:
            print("\nCPF inválido! Por favor, tente novamente.")

    return cpf
