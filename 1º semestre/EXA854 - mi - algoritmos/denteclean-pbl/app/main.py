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
            print(f"\nValor inválido. Por favor, tente novamente!\n")

if __name__== "__main__":
    main()


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
