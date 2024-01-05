from datetime import datetime

from classes.Clinic import Clinica
from classes.Session import Sessao
class Dentista(Clinica):
    def BuscarSessaoAtual(self):
        sessoes = Sessao.BuscarTodos(self)

        if not sessoes:
            return None

        dataAtual = datetime.now()
        dataAtual = dataAtual.strftime("%d/%m/%Y")

        for sessao in sessoes:
            if sessao.data == dataAtual:
                return sessao

        return None


    def AtenderProximoPaciente(self):
        print("oi")
