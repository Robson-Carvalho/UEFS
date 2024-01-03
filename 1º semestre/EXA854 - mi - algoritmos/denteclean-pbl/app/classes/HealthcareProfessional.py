import json
class HealthcareProfessional:
  def beginSession(self):
        print("\nsessão iniciada\n")

  def getAllSessions(self):
        try:
            with open("sessions.json", 'r') as file:
                sessions = json.load(file)
            return sessions
        except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
            return []


  def startAtendimento(self, session_id):
        sessions = self.getAllSessions()

        found_session = None
        for session in sessions:
            if session["id"] == session_id:
                found_session = session
                break

        if found_session:
            found_session["atendendo"] = True

            try:
               with open("sessions.json", 'w') as file:
                 json.dump(sessions, file)
            
            except Exception as e:
                  print(f"Erro ao salvar no arquivo JSON: {e}")

            print(f"\nAtendimento iniciado para a sessão com ID {session_id}.")

        else:
            print(f"\nNenhuma sessão encontrada com o ID {session_id}.")

