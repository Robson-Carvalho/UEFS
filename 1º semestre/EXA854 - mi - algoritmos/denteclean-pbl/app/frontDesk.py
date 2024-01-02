import os
import subprocess

from utils.clearTerminal import clearTerminal

from classes.FrontDesk import FrontDesk

os.system('cls' if os.name == 'nt' else 'clear')


frontDeskProfessional = FrontDesk()

def frontDesk():
  menu = 0
  while menu != 3:
    try:
        menu = int(input("Programa da Recepção\n\n1 - Criar sessão\n\n3 - Sair\n\nEscolha uma opção: "))        

        if menu != 1 and menu != 2 and menu != 3:
          os.system('cls' if os.name == 'nt' else 'clear')
          print("\nOpção inválida! Por favor, tente novamente com as opções fornecidas\n")
    except:
      os.system('cls' if os.name == 'nt' else 'clear')        
      print("\nValor inválido! Por favor, tente novamente com as opções fornecidas\n")

    if menu == 1:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("Programa da Recepção - Criação de sessão\n")

      frontDeskProfessional.beginSession()

      clearTerminal()
    
    elif menu == 2:
      os.system('cls' if os.name == 'nt' else 'clear')

      clearTerminal()
    
    elif menu == 3:
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


    


    

