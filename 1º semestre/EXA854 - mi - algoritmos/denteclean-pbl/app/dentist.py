import os

os.system('cls' if os.name == 'nt' else 'clear')

def dentist():
  start = True
  while start:
    try:
        menu = int(input("Programa do Dentista\n\n1 - Recepção\n2 - Dentista\n0 - Sair\n\nEscolha uma opção: "))

        if menu == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("1")

        elif menu == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("2")

        elif menu == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            break

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nOpção inválida! Por favor, tente novamente com as opções fornecidas\n")
    except:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nValor inválido! Por favor, tente novamente com as opções fornecidas\n")








