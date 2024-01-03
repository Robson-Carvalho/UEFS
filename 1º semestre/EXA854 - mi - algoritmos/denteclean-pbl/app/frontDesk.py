import os
import subprocess

from utils.clearTerminal import clearTerminal
from utils.getData import getData
from utils.getSchedule import getSchedule

from classes.FrontDesk import FrontDesk

os.system('cls' if os.name == 'nt' else 'clear')


frontDeskProfessional = FrontDesk()

def frontDesk():
  menu = 0
  while menu != 9:
    try:
        menu = int(input("Programa da Recepção\n\n1 - Criar sessão\n2 - Listar sessões\n3 - Buscar sessão\n4 - Consultas de uma sessão\n5 - Iniciar sessão\n9 - Sair\n\nEscolha uma opção: "))        

        if menu != 1 and menu != 2 and menu != 3 or menu != 4 or menu != 5:
          os.system('cls' if os.name == 'nt' else 'clear')
          print("\nOpção inválida! Por favor, tente novamente com as opções fornecidas\n")
    except:
      os.system('cls' if os.name == 'nt' else 'clear')        
      print("\nValor inválido! Por favor, tente novamente com as opções fornecidas\n")

    if menu == 1:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("Programa da Recepção - Criação de sessão\n")

      data = getData()
      horario = getSchedule()

      frontDeskProfessional.createSession(data, horario)

      print("\nSessão criada com sucesso!")

      clearTerminal()
    
    elif menu == 2:
      os.system('cls' if os.name == 'nt' else 'clear')

      sessions = frontDeskProfessional.getAllSessions()

      if not sessions:
        print("Não há sessões")
      else:
        print("\nTabela de Sessões:")
        print("------------------------------")
        print("| ID |   Data   |  Horário  |")
        print("------------------------------")

        for session in sessions:
            session_id = session["id"]
            data = session["data"]
            horario = session["horario"]
          
            print(f"| {session_id:2} | {data:10} | {horario} |")

        print("------------------------------")


      clearTerminal()
    
    elif menu == 3:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("Programa da Recepção - Buscando sessão\n")

      data = getData()
      horario = getSchedule()

      session = frontDeskProfessional.getSession(data, horario)

      if not session:
        print("Não há sessão com esse horário e data")
      else:
        print("\nDetalhes da Sessão:")
        print(f"ID da Sessão: {session['id']}")
        print(f"Data: {session['data']}")
        print(f"Horário: {session['horario']}")
        print(f"Atendimento: {session['atendendo']}")
        
        # Mostrar detalhes da fila de atendimento
        print("\nFila de Atendimento:")
        for paciente_id in session["fila_de_atendimento"]:
            print(f"ID do Paciente: {paciente_id}")
            # Adicione lógica para buscar e mostrar detalhes do paciente se necessário
            
        # Mostrar detalhes dos consultados
        print("\nConsultados:")
        for consultado_id in session["consultados"]:
            print(f"ID do Consultado: {consultado_id}")
            # Adicione lógica para buscar e mostrar detalhes do consultado se necessário

        # Mostrar detalhes da fila de pacientes
        print("\nFila de Pacientes:")
        for paciente_id in session["fila_de_pacientes"]:
            print(f"ID do Paciente: {paciente_id}")
            # Adicione lógica para buscar e mostrar detalhes do paciente se necessário

      clearTerminal()

    elif menu == 4:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("Programa da Recepção - Consultas de uma sessão\n")

      data = getData()
      horario = getSchedule()

      session = frontDeskProfessional.getSession(data, horario)

      if not session:
        print("Não há sessão com esse horário e data")
      else:          
        # Mostrar detalhes dos consultados
        print("\nConsultados:\n")
        for consultado_id in session["consultados"]:
            print(f"ID do Consultado: {consultado_id}")
            # Adicione lógica para buscar e mostrar detalhes do consultado se necessário

      clearTerminal()


    elif menu == 5:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("Programa da Recepção - Iniciando sessão\n")

      id = int(input("Digite o id da sessão: "))

      frontDeskProfessional.startAtendimento(id)

      clearTerminal()



    elif menu == 9:
      print("\nEncerrando sessão\n")
    
      os.system('cls' if os.name == 'nt' else 'clear')

      program_to_run = './open.py'
  
      try:
        subprocess.run(['python', program_to_run] + [], check=True)
      except:
        try:
          subprocess.run(['python3', program_to_run] + [], check=True)
        except subprocess.CalledProcessError as e:
          print(f"Erro ao executar 'dentist': {e.returncode}")
        except FileNotFoundError:
          print(f"Arquivo '{program_to_run}' não encontrado.")
        except Exception as e:
          print(f"Ocorreu um erro: {e}")


    


    

