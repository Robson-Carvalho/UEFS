import json

from.HealthcareProfessional import HealthcareProfessional

class FrontDesk(HealthcareProfessional):
  def createPatient(self):
    print("\nPaciente criado!\n")

  def createSession(self, data, horario):
        sessions = self.getAllSessions()

        if not sessions:
            sessions_obj = [{"id": 1, "data": data, "horario": horario, "atendendo": False, "fila_de_atendimento": [{}], "fila_de_pacientes": [{}], "consultados": [{}]}]
            with open("sessions.json", 'w') as file:
                json.dump(sessions_obj, file)
        else:
            try:
                last_session_id = sessions[-1]["id"]
            except KeyError:
                last_session_id = -1

            new_session_id = last_session_id + 1
            new_session = {"id": new_session_id, "data": data, "horario": horario, "atendendo": False, "fila_de_atendimento": [{}], "fila_de_pacientes": [{}], "consultados": [{}]}
            sessions.append(new_session)
          
            with open("sessions.json", 'w') as file:
                json.dump(sessions, file)

            return new_session_id

 
  def getSession(self, data, horario):
    sessions = self.getAllSessions()

    for session in sessions:
        if session["data"] == data and session["horario"] == horario:
            return session
    return {}
