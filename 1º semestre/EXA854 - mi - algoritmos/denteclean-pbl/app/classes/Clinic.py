from.Session import Sessao

class Clinica:
    def IniciarAtendimento(self, data, horario):
        Sessao.IniciarAtendimento(self, data, horario)

    def EncerrarAtendimento(self, data, horario):
        Sessao.EncerrarAtendimento(self, data, horario)
