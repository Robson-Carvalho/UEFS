import os

from dentist import dentist
from frontDesk import frontDesk

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    start = True
    while start:
        try:
            print("Seja bem-vindo ao sistema da Denteclean\n")
            i = int(input("1 - Recepção\n2 - Dentista\n0 - Sair\n\nEscolha uma opção: "))

            if i == 1:
                frontDesk()

            elif i == 2:
                dentist()
            elif i == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Sistema Denteclean encerrado!")
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nOpção inválida! Por favor, tente novamente com as opções fornecidas\n")

        except ValueError as Error:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\nMensagem de erro: {Error}!\n")

if __name__== "__main__":
    main()
