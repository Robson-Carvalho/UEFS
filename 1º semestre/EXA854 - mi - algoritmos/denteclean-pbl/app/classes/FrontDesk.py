from datetime import datetime

from utils.validateCPF import validateCPF

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
            print("Não há sessões cadastradas")
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

                print(f" {id:2} | {data} | {horario} |  {atendendo}   ")

            print("-----------------------------------------")

    def ConsultasDaSessao(self, data, horario):
        sessao = Sessao.Buscar(self, data, horario)

        if not sessao:
            print("\nNão há sessão com essa data e horário")
        else:
            if not sessao.consultados:
                print("\nNão houve consultas nesse dia!")
            else:
                print("\nTabela de Consultados:")
                print("---------------------------------------------------")
                print(f" ID | {'Nome':25}    |  CPF ")
                print("---------------------------------------------------")
                for consultado_id in sessao.consultados:
                    paciente = Paciente.BuscarPeloID(consultado_id)

                    if paciente:
                        print(f" {id:2} | {paciente.nome:25}    | {paciente.cpf} ")
                        print("---------------------------------------------------")

    def CadastrarPaciente(self, nome, cpf):
        cpfValidado = validateCPF(cpf)

        if not cpfValidado:
            return

        paciente = Paciente.BuscarPeloCPF(self, cpf)

        if paciente:
            print("\nCPF está em uso! Por favor, tente novamente")

        else:
            paciente = Paciente(0, nome, cpf)

            paciente.Criar()

    def MarcarHorarioDoPaciente(self, idSessao, cpf):
        validacao = validateCPF(cpf)

        try:
            intIdSessao = int(idSessao)
        except:
            print(f"\nValor do id inválido! Tente novamente.")
            return

        if not validacao:
            return

        paciente = Paciente.BuscarPeloCPF(self, cpf)

        if not paciente:
            print(f"\nNão há paciente cadastrado com cpf {cpf}!")
            return

        sessao = Sessao.BuscarPeloID(self, intIdSessao)

        if not sessao:
            print(f"\nNão há sessão cadastrada com o id {intIdSessao}")
            return

        dataAtual = datetime.now()
        dataAtual = dataAtual.strftime("%d/%m/%Y")

        if dataAtual > sessao.data:
            print("\nSessão indisponível para marcação de horário!")
            return

        totalDePacientesNaSessao = len(sessao.fila_de_atendimento) + len(sessao.consultados) + len(sessao.fila_de_pacientes)

        if totalDePacientesNaSessao >= 6:
            print(f"\nSessão já está completa! Por favor, criei uma nova sessão para o cadastro de {paciente.nome}")
            return

        if intIdSessao in sessao.fila_de_pacientes or intIdSessao in sessao.fila_de_atendimento or intIdSessao in sessao.consultados:
            print(f"\nO paciente {paciente.nome} já tem horário marcado para essa sesão! Por favor, marque para uma próxima sessão.")
            return

        Sessao.MarcarHorarioDoPaciente(self, intIdSessao, paciente)

    def ListarPacientes(self):
        pacientes = Paciente.BuscarTodos(self)

        if not pacientes:
            print("Não há pacientes cadastrados")
        else:
            print("Tabela de Pacientes:")
            print("---------------------------------------------------")
            print(f" ID | {'Nome':25}    |  CPF ")
            print("---------------------------------------------------")
            for paciente in pacientes:
                id = paciente.id
                nome = paciente.nome
                cpf = paciente.cpf

                print(f" {id:2} | {nome:25}    | {cpf} ")
                print("---------------------------------------------------")

    def ListarHorariosPaciente(self, cpf):
        validacao = validateCPF(cpf)

        if not validacao:
            return

        paciente = Paciente.BuscarPeloCPF(self, cpf)

        if not paciente:
            print(f"\nNão há paciente cadastrado com cpf {cpf}!")
            return

        horarios = []
        sessoes = Sessao.BuscarTodos(self)

        for sessao in sessoes:
            if paciente.id in sessao.fila_de_atendimento or paciente.id in sessao.fila_de_pacientes or paciente.id in sessao.consultados:
                horarios.append({"data": sessao.data, "horario": sessao.horario})

        if not horarios:
            print(f"\nNão há horários cadastrados para esse paciente {paciente.nome}")
            return


        print(f"\nHorários do paciente {paciente.nome}:\n")
        print("-----------------------")
        print(f" {'Data':9} | Horário")
        print("-----------------------")
        for horario in horarios:
            print(f"{horario['data']} | {horario['horario']}")
            print("-----------------------")

    def VerificarPacienteSessaoAtual(self, cpf):
        validacao = validateCPF(cpf)

        if not validacao:
            return

        paciente = Paciente.BuscarPeloCPF(self, cpf)

        if not paciente:
            print(f"\nNão há paciente cadastrado com o cpf {cpf}")
            return

        sessoes = Sessao.BuscarTodos(self)

        if not sessoes:
            print("\nA clinica ainda não possui nenhuma sessão cadastrada.")
            return
        else:
            dataAtual = datetime.now()
            dataAtual = dataAtual.strftime("%d/%m/%Y")
            for sessao in sessoes:
                if sessao.data == dataAtual:
                    if paciente.id in sessao.fila_de_pacientes:
                        print(f"\nPaciente {paciente.nome} tem horário para sessão de hoje!")
                        return
                    else:
                        print(f"\nPaciente {paciente.nome} não tem horário marcado para sessão de hoje!")
                        return

        print("\nNão há sessão cadastrada para hoje.")

    def ColocarNaFilaDeAtendimento(self, cpf):
        validacao = validateCPF(cpf)

        if not validacao:
            return

        paciente = Paciente.BuscarPeloCPF(self, cpf)

        if not paciente:
            print(f"\nNão há paciente cadastrado com o cpf {cpf}")
            return

        sessoes = Sessao.BuscarTodos(self)

        if not sessoes:
            print("\nA clinica ainda não possui nenhuma sessão cadastrada.")
            return
        else:
            dataAtual = datetime.now()
            dataAtual = dataAtual.strftime("%d/%m/%Y")
            for sessao in sessoes:
                if sessao.data == dataAtual:
                    if paciente.id in sessao.fila_de_atendimento:
                        print(f"\nPaciente {paciente.nome} já está na fila de atendimento.")
                        return

                    if paciente.id in sessao.fila_de_pacientes:
                        if sessao.atendendo:
                            Sessao.ColocarNaFilaDeAtendimento(self, sessao.id, paciente)
                            return

                        else:
                            print("\nA sessão não está iniciada para atendimento! Por favor, iniciei antes desse procedimento.")
                            return

                    else:
                        print(f"\nPaciente {paciente.nome} não está cadastrado para esse sessão!")
                        return

            print("\nNão há sessão cadastrada para hoje.")

    def ProximoPacienteParaAtendimento(self):
        sessoes = Sessao.BuscarTodos(self)

        if not sessoes:
            print("A clinica ainda não possui nenhuma sessão cadastrada.")
            return
        else:
            dataAtual = datetime.now()
            dataAtual = dataAtual.strftime("%d/%m/%Y")
            for sessao in sessoes:
                if sessao.data == dataAtual:
                    if sessao.fila_de_atendimento:
                        proximoPaciente = sessao.fila_de_atendimento[0]

                        paciente = Paciente.BuscarPeloID(self, proximoPaciente)

                        if not paciente:
                            print("Erro ao buscar paciente.")
                            return

                        print(f"O próximo paciente para atendimento é {paciente.nome}.")
                        return
                    else:
                        print(f"Não há pacientes na fila de atendimento atual.")
                        return

        print("Não há sessão cadastrada para hoje.")
