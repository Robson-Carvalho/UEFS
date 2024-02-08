from database.utils import LerPacienteBancoDeDados
from database.utils import SalvarPacienteBancoDeDados
class Paciente:
    def __init__(self, id, nome, cpf, prontuario=None):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.prontuario = prontuario or []

    def Criar(self):
        pacientes = self.BuscarTodos()

        if not pacientes:
            somarID = 0
        else:
            try:
                somarID = pacientes[-1].id
            except AttributeError:
                somarID = -1

        novoID = somarID + 1

        novoPaciente = Paciente(novoID, self.nome, self.cpf, [])
        novoPaciente.id = novoID
        pacientes.append(novoPaciente)


        resultado = SalvarPacienteBancoDeDados(pacientes)

        if resultado == 1:
            print("\nPaciente criado com sucesso!")

        if resultado == 2:
            print("\nErro ao criar paciente!")

        if resultado == 3:
            print("\nPaciente não fornecida!")

    def Salvar(pacientes):
        resultado = SalvarPacienteBancoDeDados(pacientes)

        if resultado == 1:
            print("\nAnotação salva com sucesso!")

        if resultado == 2:
            print("\nErro ao salvar anotação!")

        if resultado == 3:
            print("\nPacientes não fornecidos")

    def BuscarTodos(self):
        return LerPacienteBancoDeDados(Paciente)

    def BuscarPeloID(self, id):
        pacientes = Paciente.BuscarTodos(self)

        if not pacientes:
            return None

        for paciente in pacientes:
            if paciente.id == id:
                return paciente

        return None

    def BuscarPeloCPF(self, cpf):
        pacientes = Paciente.BuscarTodos(self)

        if not pacientes:
            return None

        for paciente in pacientes:
            if paciente.cpf == cpf:
                return paciente

        return None


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
