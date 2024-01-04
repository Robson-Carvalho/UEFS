import json

class Sessao:
    def __init__(self, id, data, horario, atendendo = False, fila_de_atendimento = [], fila_de_pacientes = [], consultados = []):
        self.id = id
        self.data = data
        self.horario =horario
        self.atendendo = atendendo or False
        self.fila_de_atendimento = fila_de_atendimento or []
        self.fila_de_pacientes = fila_de_pacientes or []
        self.consultados = consultados or []

    def Criar(self):
        sessoes = self.BuscarTodos()

        if not sessoes:
                somarID = 0
        else:
            try:
                somarID = sessoes[-1].id
            except AttributeError:
                somarID = -1

        novoID = somarID + 1

        novaSessao = Sessao(novoID, self.data, self.horario)
        novaSessao.id = novoID
        sessoes.append(novaSessao)

        with open("sessions.json", 'w') as file:
            json.dump([sessao.__dict__ for sessao in sessoes], file)

    def BuscarTodos(self):
        try:
            with open("sessions.json", 'r') as file:
                sessoes = json.load(file)
            resultado = [Sessao(**sessao) for sessao in sessoes]
            return resultado
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            return []

    def BuscarPeloID(self, id):
        sessoes = Sessao.BuscarTodos(self)

        sessaoEncontrada = None
        for sessao in sessoes:
            if sessao.id == id:
                sessaoEncontrada = sessao
                break

        return sessaoEncontrada

    def IniciarAtendimento(self, data, horario):
        sessoes = Sessao.BuscarTodos(self)

        sessaoEncontrada = None
        for sessao in sessoes:
            if sessao.data == data and sessao.horario == horario:
                sessaoEncontrada = sessao
                break

        if sessaoEncontrada:
            sessaoEncontrada.atendendo = True

            try:
               with open("sessions.json", 'w') as file:
                 json.dump([sessao.__dict__ for sessao in sessoes], file)

            except Exception as e:
                  print(f"Erro ao salvar no arquivo JSON: {e}")

            print(f"\nAtendimento iniciado para a sessão com ID {sessao.id}.")

        else:
            print(f"\nNenhuma sessão encontrada.")

    def EncerrarAtendimento(self, data, horario):
        sessoes = Sessao.BuscarTodos(self)

        sessaoEncontrada = None
        for sessao in sessoes:
            if sessao.data == data and sessao.horario == horario:
                sessaoEncontrada = sessao
                break

        if sessaoEncontrada:
            sessaoEncontrada.atendendo = False

            try:
               with open("sessions.json", 'w') as file:
                 json.dump([sessao.__dict__ for sessao in sessoes], file)

            except Exception as e:
                  print(f"\nErro ao salvar no arquivo JSON: {e}")

            print(f"\nAtendimento encerrado para a sessão com ID {sessao.id}.")

        else:
            print(f"\nNenhuma sessão encontrada.")

    def MarcarHorarioDoPaciente(self, idSessao, paciente):
        sessoes = Sessao.BuscarTodos(self)

        sessaoEncontrada = None
        for sessao in sessoes:
            if sessao.id == idSessao:
                sessaoEncontrada = sessao
                break

        if sessaoEncontrada:
            sessaoEncontrada.fila_de_pacientes.append(paciente.id)

            try:
                with open("sessions.json", 'w') as file:
                    json.dump([sessao.__dict__ for sessao in sessoes], file)

            except Exception as e:
                print(f"\nErro ao salvar no arquivo JSON: {e}")

            print(f"\nMarcação de horário para {paciente.nome} realizada com sucesso.")

        else:
            print(f"\nNenhuma sessão encontrada.")

    def Buscar(self, data, horario):
        sessoes = Sessao.BuscarTodos(self)

        for sessao in sessoes:
            if sessao.data == data and sessao.horario == horario:
                return sessao
        return None
