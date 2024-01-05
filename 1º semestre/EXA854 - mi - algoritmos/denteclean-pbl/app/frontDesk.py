import os

from utils.getData import getData
from utils.getSchedule import getSchedule
from utils.clearTerminal import clearTerminal

from classes.FrontDesk import FrontDesk

classFrontDesk = FrontDesk()

def frontDesk():
    os.system('cls' if os.name == 'nt' else 'clear')
    start = True
    while start:

            menu = int(input(f"Programa da Recepção\n\n1 - Criar sessão\n2 - Listar sessões\n3 - Buscar sessão\n4 - Consultas de uma sessão\n5 - Iniciar sessão\n6 - Encerrar sessão\n7 - Cadastrar paciente\n8 - Marca horário para paciente\n9 - Listar pacientes\n10 - Horários do paciente\n11 - Verificar se paciente tem horário na sessão atual\n12 - Colocar paciente na fila de atendimento\n13 - Listar próximo paciente da fila de atendimento\n0 - Sair\n\nEscolha uma opção: "))

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

                nome = input("Digite o nome paciente: ")

                cpf = input("Digite o número do CPF do paciente: ")

                classFrontDesk.CadastrarPaciente(nome, cpf)

                clearTerminal()

            elif menu == 8:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Programa da Recepção - Marca horário para paciente\n")

                idSessao = input("Digite o ID da sessão: ")

                cpf = input("Digite o número do CPF do paciente: ")

                classFrontDesk.MarcarHorarioDoPaciente(idSessao, cpf)

                clearTerminal()

            elif menu == 9:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Programa da Recepção - Listar pacientes\n")

                classFrontDesk.ListarPacientes()

                clearTerminal()

            elif menu == 10:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Programa da Recepção - Listar horários do paciente\n")

                cpf = input("Digite o número do CPF do paciente: ")

                classFrontDesk.ListarHorariosPaciente(cpf)

                clearTerminal()

            elif menu == 11:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Programa da Recepção - Verifica se paciente tem horário na sessão atual\n")

                cpf = input("Digite o número do CPF do paciente: ")

                classFrontDesk.VerificarPacienteSessaoAtual(cpf)

                clearTerminal()

            elif menu == 12:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Programa da Recepção - Colocar paciente na fila de atendimento\n")

                cpf = input("Digite o número do CPF do paciente: ")

                classFrontDesk.ColocarNaFilaDeAtendimento(cpf)

                clearTerminal()

            elif menu == 13:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Programa da Recepção - Próximo paciente a ser atendido\n")

                classFrontDesk.ProximoPacienteParaAtendimento()

                clearTerminal()

            elif menu == 0:
                os.system('cls' if os.name == 'nt' else 'clear')
                break

            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("\nOpção inválida! Por favor, tente novamente com as opções fornecidas\n")

