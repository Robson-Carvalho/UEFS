from datetime import datetime

from database.utils import SalvarSessaoBancoDeDados
from database.utils import LerSessoesBancoDeDados

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

        dataAtual = datetime.now()
        dataAtual = dataAtual.strftime("%d/%m/%Y")

        # Converte a hora atual para o mesmo formato da hora armazenada em self.data
        horarioAtual = datetime.now().time()
        horarioAtual = horarioAtual.strftime("%H:%M:%S")

        if dataAtual > self.data:
            print("\nNão foi possível criar a sessão! Só é permitido a criação com a data partir da data atual.")
            return

        if dataAtual == self.data and horarioAtual > self.horario:
            print(f"\nNão foi possível criar a sessão! São {horarioAtual}, criei uma sessão com um horário posterior.")
            return

        if not sessoes:
                somarID = 0
        else:
            for sessao in sessoes:
                if sessao.data == self.data:
                    print("\nJá existe sessão com essa data! Por favor, cadastre em um dia diferente.")
                    return

            try:
                somarID = sessoes[-1].id
            except AttributeError:
                somarID = -1

        novoID = somarID + 1
        novaSessao = Sessao(novoID, self.data, self.horario)
        novaSessao.id = novoID
        sessoes.append(novaSessao)

        resultado = SalvarSessaoBancoDeDados(sessoes)

        if resultado == 1:
            print("\nSessão criada com sucesso!")

        if resultado == 2:
            print("\nErro ao salvar sessão!")

        if resultado == 3:
            print("\nSessão não fornecida!")

    def BuscarTodos(self):
        return LerSessoesBancoDeDados(Sessao)

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
            dataAtual = datetime.now()
            dataAtual = dataAtual.strftime("%d/%m/%Y")

            if sessaoEncontrada.data != dataAtual:
                print("\nSomente a sessão do dia atual pode ser inciada!")
                return
            sessaoEncontrada.atendendo = True

            resultado = SalvarSessaoBancoDeDados(sessoes)

            if resultado == 1:
                print("\nSessão iniciada com sucesso!")

            if resultado == 2:
                print("\nErro ao iniciar sessão!")

            if resultado == 3:
                print("\nSessão não fornecida!")
        else:
            print("\nSessão não encontrada")

    def EncerrarAtendimento(self, data, horario):
        sessoes = Sessao.BuscarTodos(self)

        sessaoEncontrada = None
        for sessao in sessoes:
            if sessao.data == data and sessao.horario == horario:
                sessaoEncontrada = sessao
                break

        if sessaoEncontrada:
            sessaoEncontrada.atendendo = False

            resultado = SalvarSessaoBancoDeDados(sessoes)

            if resultado == 1:
                print("\nSessão encerrada com sucesso!")

            if resultado == 2:
                print("\nErro ao encerrada sessão!")

            if resultado == 3:
                print("\nSessão não fornecida!")
        else:
            print("\nSessão não encontrada")

    def MarcarHorarioDoPaciente(self, idSessao, paciente):
        sessoes = Sessao.BuscarTodos(self)

        sessaoEncontrada = None
        for sessao in sessoes:
            if sessao.id == idSessao:
                sessaoEncontrada = sessao
                break

        if sessaoEncontrada:
            sessaoEncontrada.fila_de_pacientes.append(paciente.id)

            resultado = SalvarSessaoBancoDeDados(sessoes)

            if resultado == 1:
                print("\nHorário marcado com com sucesso!")

            if resultado == 2:
                print("\nErro ao marcar horário!")

            if resultado == 3:
                print("\nSessão não fornecida!")
        else:
            print("\nSessão não encontrada")

    def Buscar(self, data, horario):
        sessoes = Sessao.BuscarTodos(self)

        for sessao in sessoes:
            if sessao.data == data and sessao.horario == horario:
                return sessao
        return None

    def ColocarNaFilaDeAtendimento(self, idSessao, paciente):
        sessoes = Sessao.BuscarTodos(self)

        sessaoEncontrada = None

        for sessao in sessoes:
            if sessao.id == idSessao:
                sessaoEncontrada = sessao
                break

        if sessaoEncontrada:
            sessaoEncontrada.fila_de_pacientes.remove(paciente.id)
            sessaoEncontrada.fila_de_atendimento.append(paciente.id)

            resultado = SalvarSessaoBancoDeDados(sessoes)

            if resultado == 1:
                print(f"\nPaciente {paciente.nome} colocado na fila de atendimento!")

            if resultado == 2:
                print("\nErro colocar paciente na fila de atendimento!")

            if resultado == 3:
                print("\nSessão não fornecida!")
        else:
            print("\nSessão não encontrada")
