import json

class Patient:
    def __init__(self, id, nome, cpf, prontuario=None):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.prontuario = prontuario or []

    def Create(self):
        patients = self.GetAllPatient()

        if not patients:
            sumID = 0
        else:
            try:
                sumID = patients[-1].id
            except AttributeError:
                sumID = -1

        newID = sumID + 1

        new_patient = Patient(newID, self.nome, self.cpf, [])
        new_patient.id = newID
        patients.append(new_patient)

        with open("patients.json", 'w') as file:
            json.dump([patient.__dict__ for patient in patients], file)


    def GetAllPatient(self):
      try:
        with open("patients.json", 'r') as file:
          patients_data = json.load(file)
        patients = [Patient(**patient) for patient in patients_data]
        return patients
      except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            return []

        