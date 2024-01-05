import os

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
            menu = int(input(f"Programa do Dentista\n\n{1:02d} - Localizar sessão\n{2:02d} - Iniciar sessão\n0 - Sair\n\nEscolha uma opção: "))

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

            elif menu == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                break

            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Opção inválida! Por favor, tente novamente com as opções fornecidas\n")

        except ValueError as e:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Erro! Por favor, tente novamente. {e}\n")


