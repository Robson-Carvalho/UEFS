from.Clinic import Clinica
from.Session import Sessao
from.Patient import Paciente

class FrontDesk(Clinica):
    def CriarSessao(self, data, horario):
        sessao = Sessao(0, data, horario)

        sessao.Criar()

        print("\nSessão criada com sucesso!")

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

    def BuscarSessao(self, data, horario):
      sessao = Sessao.Buscar(self, data, horario)

      if not sessao:
        print("Não há sessão com esse horário e data")
      else:
        print("\nDetalhes da Sessão:")
        print(f"ID da Sessão: {sessao.id}")
        print(f"Data: {sessao.data}")
        print(f"Horário: {sessao.horario}")
        print(f"Atendimento: {sessao.atendendo}")

        # Mostrar detalhes da fila de atendimento
        print("\nFila de Atendimento:")
        for paciente_id in sessao.fila_de_atendimento:
            print(f"ID do Paciente: {paciente_id}")
            # Adicione lógica para buscar e mostrar detalhes do paciente se necessário

        # Mostrar detalhes dos consultados
        print("\nConsultados:")
        for consultado_id in sessao.consultados:
            print(f"ID do Consultado: {consultado_id}")
            # Adicione lógica para buscar e mostrar detalhes do consultado se necessário

        # Mostrar detalhes da fila de pacientes
        print("\nFila de Pacientes:")
        for paciente_id in sessao.fila_de_pacientes:
            print(f"ID do Paciente: {paciente_id}")
            # Adicione lógica para buscar e mostrar detalhes do paciente se necessário

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
            paciente = Paciente(0, nome, cpf)

            paciente.Criar()

            print(f"\nPaciente {nome} cadastrado com sucesso!")
