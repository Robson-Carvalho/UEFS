import os

from functions.dentistMenu import dentistMenu

from utils.getData import getData
from utils.getSchedule import getSchedule
from utils.clearTerminal import clearTerminal

from classes.Dentist import Dentista

classDentist = Dentista

def dentist():
    os.system('cls' if os.name == 'nt' else 'clear')
    start = True
    while start:
        try:

            menu = int(input(f"Programa do Dentista\n\n1 - Localizar sessão\n2 - Iniciar sessão\n3 - Atender próximo paciente\n0 - Sair\n\nEscolha uma opção: "))

            if menu == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Programa do Dentista - Localizar sessão\n")

                data = getData()
                horario = getSchedule()

                classDentist.BuscarSessao("", data, horario)

                clearTerminal()

            elif menu == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Programa da Recepção - Iniciando sessão\n")

                data = getData()
                horario = getSchedule()

                classDentist.IniciarAtendimento("", data, horario)

                clearTerminal()

            elif menu == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Programa da Recepção - Atender próximo paciente\n")

                classDentist.AtenderProximoPaciente()

            elif menu == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                break

            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nOpção inválida! Por favor, tente novamente com as opções fornecidas\n")

        except ValueError as e:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nOpção inválida. Por favor, tente novamente!\n")

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
