from datetime import datetime

from.Clinic import Clinica
from.Session import Sessao
from.Patient import Paciente

class FrontDesk(Clinica):
    def CriarSessao(self, data, horario):
        sessao = Sessao(0, data, horario)

        sessao.Criar()

    def ListarSessoes(self):
        sessoes = Sessao.BuscarTodos(self)

        if not sessoes:
            print("Não há sessões")
        else:
            print("\nTabela de Sessões:")
            print("-----------------------------------------")
            print(" ID |    Data    |  Horário | Atendendo")
            print("-----------------------------------------")

            for sessao in sessoes:
                id = sessao.id
                data = sessao.data
                horario = sessao.horario
                atendendo = sessao.atendendo
                filaPacientes = sessao.fila_de_pacientes
                filaAtendimento = sessao.fila_de_atendimento
                consultados = sessao.consultados

                print(f" {id:2} | {data} | {horario} |  {atendendo}   ")

            print("-----------------------------------------")


    def ConsultasDaSessao(self, data, horario):
        sessao = Sessao.Buscar(self, data, horario)

        if not sessao:
            print("\nNão há sessão com esse horário e data")
        else:
            if not sessao.consultados:
                print("\nNão houve consultas nesse dia!")
            else:
                print("\nConsultados:\n")
                for consultado_id in sessao.consultados:
                    print(f"ID do Consultado: {consultado_id}")
                    # Tarefa - Adicionar lógica para buscar e mostrar detalhes do consultado

    def CadastrarPaciente(self, nome, cpf):
        paciente = Paciente.BuscarPeloCPF(self, cpf)

        if paciente:
            print("\nCPF indisponível! Por favor, tente outro")

        else:
            paciente = Paciente(0, nome, cpf)

            paciente.Criar()


    def MarcarHorarioDoPaciente(self, idSessao, cpf):
        paciente = Paciente.BuscarPeloCPF(self, cpf)

        if not paciente:
            print("\nPaciente não cadastrado!")
            return

        sessao = Sessao.BuscarPeloID(self, idSessao)

        if not sessao:
            print("\nSessão não cadastrado!")
            return


        dataAtual = datetime.now()
        dataAtual = dataAtual.strftime("%d/%m/%Y")

        if dataAtual < sessao.data:
            print("\nSessão indisponível!")
            return

        totalDePacientesNaSessao = len(sessao.fila_de_atendimento) + len(sessao.consultados) + len(sessao.fila_de_pacientes)

        if totalDePacientesNaSessao >= 6:
            print("\nSessão completa! Por favor, criei uma nova sessão para o cadastro de mais pacientes")
            return

        Sessao.MarcarHorarioDoPaciente(self, idSessao, paciente)

    def ListarPacientes(self):
        pacientes = Paciente.BuscarTodos(self)

        if not pacientes:
            print("\nNão há pacientes cadastrados")
        else:
            print("\nTabela de Pacientes:")
            print("---------------------------------------------------")
            print(f" ID | {'Nome':25}    |  CPF ")
            print("---------------------------------------------------")

            for paciente in pacientes:
                id = paciente.id
                nome = paciente.nome
                cpf = paciente.cpf

                print(f" {id:2} | {nome:25}    | {cpf} ")

            print("---------------------------------------------------")

    def  ListarHorariosPaciente():
        print("Oi")







