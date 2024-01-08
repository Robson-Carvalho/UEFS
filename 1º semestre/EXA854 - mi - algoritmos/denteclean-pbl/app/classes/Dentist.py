from datetime import datetime

from functions.dentistMenu import dentistMenu

from classes.Clinic import Clinica
from classes.Session import Sessao
class Dentista(Clinica):
    def BuscarSessaoAtual():
        sessoes = Sessao.BuscarTodos()

        if not sessoes:
            return None

        dataAtual = datetime.now()
        dataAtual = dataAtual.strftime("%d/%m/%Y")

        for sessao in sessoes:
            if sessao.data == dataAtual:
                return sessao

        return None

    def AtenderProximoPaciente():
        dentistMenu()
