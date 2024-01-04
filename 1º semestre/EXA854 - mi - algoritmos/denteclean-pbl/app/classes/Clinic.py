from.Session import Sessao

class Clinica:
    def IniciarAtendimento(self, data, horario):
        Sessao.IniciarAtendimento(self, data, horario)

    def EncerrarAtendimento(self, data, horario):
        Sessao.EncerrarAtendimento(self, data, horario)

    def BuscarSessao(self, data, horario):
        sessao = Sessao.Buscar(self, data, horario)
        if not sessao:
            print("Não há sessão com esse horário e data")
        else:
            print("\nDetalhes da Sessão:")
            print(f"ID da Sessão: {sessao.id}")
            print(f"Data: {sessao.data}")
            print(f"Horário: {sessao.horario}")
            print(f"\nAtendimento: {sessao.atendendo}")

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
