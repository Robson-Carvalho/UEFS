import os
from datetime import datetime

from utils.clearTerminal import clearTerminal

from classes.Anotacao import Anotacao
from classes.Session import Sessao
from classes.Patient import Paciente

def dentistMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    start = True

    dataAtual = datetime.now()
    dataAtual = dataAtual.strftime("%d/%m/%Y")

    sessoes = Sessao.BuscarTodos("self")

    if not sessoes:
        print("Programa do Dentista\n")
        print("Não há sessão cadastrada")
        clearTerminal()
        return

    sessaoAtual = {}
    for sessao in sessoes:
        if sessao.data == dataAtual:
            sessaoAtual = sessao

    if not sessaoAtual:
        print("Programa do Dentista\n")
        print("Não há sessão cadastrada")
        clearTerminal()
        return

    if not sessaoAtual.fila_de_atendimento:
        print("Programa do Dentista\n")
        print("Não há pacientes na fila de atendimento")
        clearTerminal()
        return

    if not sessaoAtual.atendendo:
        print("Programa do Dentista\n")
        print("Sessão ainda não está atendendo")
        clearTerminal()
        return

    idProximoPaciente = sessaoAtual.fila_de_atendimento[0]
    pacientes = Paciente.BuscarTodos("self")

    if not pacientes:
        print("Programa do Dentista\n")
        print("Não há pacientes cadastrados")
        clearTerminal()
        return

    pacienteAtual = {}

    for paciente in pacientes:
        if paciente.id == idProximoPaciente:
            pacienteAtual = paciente

    if not pacienteAtual:
        print("Não há pacientes cadastrados para hoje")
        return

    sessaoAtual.fila_de_atendimento.remove(pacienteAtual.id)
    sessaoAtual.consultados.append(pacienteAtual.id)

    resultado = Sessao.Salvar(sessoes)

    if not resultado:
        print("Programa do Dentista\n")
        print("Erro ao salvar paciente na lista de consultados da sessão")
        clearTerminal()
        return

    while start:
        try:
            print("Programa do Dentista - Atendimento\n")
            menu = int(input(f"Consulta do paciente {pacienteAtual.nome}\n\n1 - Ler prontuário completo\n2 - Ler primeira anotação do paciente\n3 - Ler última anotação do paciente\n4 - Anotar no protuário do paciente\n0 - Finalizar consulta\n\nEscolha uma opção: "))

            if menu == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Programa do Dentista - Atendimento - Ler prontuário completo\n")

                if not pacienteAtual.prontuario:
                    print("Não há anotações passadas")

                    clearTerminal()
                else:
                    for anotacao in pacienteAtual.prontuario:
                        print(f"{anotacao['data']} - {anotacao['horario']} - {anotacao['notas']}")


                    clearTerminal()

            elif menu == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Programa do Dentista - Atendimento - Ler primeiro prontuário\n")

                if not pacienteAtual.prontuario:
                    print("Não há anotações passadas")

                    clearTerminal()
                else:
                    anotacao = pacienteAtual.prontuario[0]
                    print(f"{anotacao['data']} - {anotacao['horario']} - {anotacao['notas']}")


                    clearTerminal()

            elif menu == 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Programa do Dentista - Atendimento - Ler último prontuário\n")

                if not pacienteAtual.prontuario:
                    print("Não há anotações passadas")

                    clearTerminal()
                else:
                    anotacao = pacienteAtual.prontuario[-1]
                    print(f"{anotacao['data']} - {anotacao['horario']} - {anotacao['notas']}")


                    clearTerminal()

            elif menu == 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Programa do Dentista - Atendimento - Anotar no prontuário do paciente\n")

                notas = input("Digite a nota do paciente: ")

                novaAnotacao = {
                    'data': sessaoAtual.data,
                    'horario': sessaoAtual.horario,
                    'notas': notas
                }

                pacienteAtual.prontuario.append(novaAnotacao)

                Paciente.Salvar(pacientes)

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
