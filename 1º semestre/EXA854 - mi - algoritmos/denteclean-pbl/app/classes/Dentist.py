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

"""
Autor: Robson Carvalho de Souza

Componente Curricular: EXA 854-MI-Algoritmos

Concluido em: 08/02/2024

Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
"""

