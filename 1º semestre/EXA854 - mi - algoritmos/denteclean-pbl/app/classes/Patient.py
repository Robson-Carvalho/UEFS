import json

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

        with open("patients.json", 'w') as file:
            json.dump([paciente.__dict__ for paciente in pacientes], file)

    def BuscarTodos(self):
      try:
        with open("patients.json", 'r') as file:
          pacientes = json.load(file)
        resultado = [Paciente(**paciente) for paciente in pacientes]
        return resultado
      except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            return []

    def BuscarPeloCPF(self, cpf):
        pacientes = Paciente.BuscarTodos(self)

        if not pacientes:
            return None

        for paciente in pacientes:
            if paciente.cpf == cpf:
                return paciente

        return None



