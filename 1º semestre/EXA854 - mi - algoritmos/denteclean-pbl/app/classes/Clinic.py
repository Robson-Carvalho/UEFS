from classes.Patient import Paciente
from.Session import Sessao

class  Clinica:
    def IniciarAtendimento(self, data, horario):
        Sessao.IniciarAtendimento(self, data, horario)

    def EncerrarAtendimento(self, data, horario):
        Sessao.EncerrarAtendimento(self, data, horario)

    def BuscarSessao(self, data, horario):
        sessao = Sessao.Buscar(self, data, horario)

        if not sessao:
            print("\nNão há sessão com essa data e horário")
            return
        else:
            print("\nDetalhes da Sessão:\n")
            print(f"ID: {sessao.id}")
            print(f"Data: {sessao.data}")
            print(f"Horário: {sessao.horario}")
            print(f"\nAtendimento: {sessao.atendendo}")

            # Mostrar detalhes da fila de pacientes
            print("\nFila de pacientes da sessão:")
            if not sessao.fila_de_atendimento:
                print("\nNão há pacientes")
            else:
                print("---------------------------------------------------")
                print(f" ID | {'Nome':25}    |  CPF ")
                print("---------------------------------------------------")

                for paciente_id in sessao.fila_de_pacientes:
                    paciente = Paciente.BuscarPeloID(paciente_id)
                    print(f" {paciente.id:2} | {paciente.nome:25}    | {paciente.cpf} ")
                    print("---------------------------------------------------")
                # Adicione lógica para buscar e mostrar detalhes do paciente se necessário


            # Mostrar detalhes da fila de atendimento
            print("\nFila de Atendimento:")
            if not sessao.fila_de_atendimento:
                print("\nNão há pacientes na fila de atendimento")
            else:
                for paciente_id in sessao.fila_de_atendimento:
                    print(f"ID do Paciente: {paciente_id}")
                    # Adicione lógica para buscar e mostrar detalhes do paciente se necessário

              # Mostrar detalhes dos consultados
            print("\nConsultados:")
            if not sessao.fila_de_atendimento:
                print("\nNão há pacientes consultados")
            else:
                for consultado_id in sessao.consultados:
                    print(f"ID do Consultado: {consultado_id}")
                # Adicione lógica para buscar e mostrar detalhes do consultado se necessário
