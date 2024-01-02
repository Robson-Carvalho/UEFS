import subprocess
import os

os.system('cls' if os.name == 'nt' else 'clear')

def dentist():
  menu = 0
  while menu != 3:
    try:
        menu = int(input("Programa do Dentista\n\n1 - Recepção\n2 - Dentista\n3 - Sair\n\nEscolha uma opção: "))        

        if menu != 1 and menu != 2 and menu != 3:
          os.system('cls' if os.name == 'nt' else 'clear')
          print("\nOpção inválida! Por favor, tente novamente com as opções fornecidas\n")
    except:
      os.system('cls' if os.name == 'nt' else 'clear')        
      print("\nValor inválido! Por favor, tente novamente com as opções fornecidas\n")

    if menu == 1:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("oi")
    if menu == 2:
      os.system('cls' if os.name == 'nt' else 'clear')
      print("oi")
    if menu == 3:
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



    

