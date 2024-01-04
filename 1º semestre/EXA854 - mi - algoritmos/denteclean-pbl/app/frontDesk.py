import os
import subprocess

from utils.validateCPF import validateCPF
from utils.getData import getData
from utils.getSchedule import getSchedule
from utils.clearTerminal import clearTerminal

from classes.FrontDesk import FrontDesk

classFrontDesk = FrontDesk()

def frontDesk():
    start = True
    while start:
        try:
            menu = int(input("Programa da Recepção\n\n1 - Criar sessão\n2 - Listar sessões\n3 - Buscar sessão\n4 - Consultas de uma sessão\n5 - Iniciar sessão\n6 - Encerrar sessão\n7 - Cadastrar paciente\n9 - Sair\n\nEscolha uma opção: "))

            if menu < 1 or menu > 9:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nOpção inválida! Por favor, tente novamente com as opções fornecidas\n")
        except:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nValor inválido! Por favor, tente novamente com as opções fornecidas\n")


        if menu == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Programa da Recepção - Criação de sessão\n")

            data = getData()
            horario = getSchedule()

            classFrontDesk.CriarSessao(data, horario)

            clearTerminal()

        elif menu == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Programa da Recepção - Listar sessões\n")


            classFrontDesk.ListarSessoes()


            clearTerminal()

        elif menu == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Programa da Recepção - Buscando sessão\n")

            data = getData()
            horario = getSchedule()


            classFrontDesk.BuscarSessao(data, horario)

            clearTerminal()

        elif menu == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Programa da Recepção - Consultas de uma sessão\n")

            data = getData()
            horario = getSchedule()

            classFrontDesk.ConsultasDaSessao(data, horario)

            clearTerminal()

        elif menu == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Programa da Recepção - Iniciando sessão\n")

            data = getData()
            horario = getSchedule()

            classFrontDesk.IniciarAtendimento(data, horario)

            clearTerminal()

        elif menu == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Programa da Recepção - Encerrando sessão\n")

            data = getData()
            horario = getSchedule()

            classFrontDesk.EncerrarAtendimento(data, horario)

            clearTerminal()


        elif menu == 7:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Programa da Recepção - Cadastro de paciente\n")

            nome = ""
            while len(nome) <= 2:
                nome = input("Digite o nome do paciente: ")

            if len(nome) <= 2:
                print("\nNome precisa ter 3 caracteres! Por favor, tente novamente.\n")


            cpf = False
            while cpf == False:
                cpf = input("\nDigite o cpf do paciente: ")
                cpf = validateCPF(cpf)

            if cpf == False:
                print("\nCPF inválido! Por favor, tente novamente.")


            classFrontDesk.CadastrarPaciente(nome, cpf)

            clearTerminal()



        elif menu == 9:
            start = False

    os.system('cls' if os.name == 'nt' else 'clear')

    program_to_run = './open.py'

    try:
        subprocess.run(['python', program_to_run] + [], check=True)
    except:
        try:
            subprocess.run(['python3', program_to_run] + [], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Erro ao executar 'dentist': {e.returncode}")
        except FileNotFoundError:
            print(f"Arquivo '{program_to_run}' não encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")







