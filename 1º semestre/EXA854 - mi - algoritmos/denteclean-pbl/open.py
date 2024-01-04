import subprocess
import os

program_to_run = './app/main.py'

os.system('cls' if os.name == 'nt' else 'clear')
start = True
while start:
    print("Seja bem-vindo ao sistema da Denteclean\n")
    i = input("1 - Recepção\n2 - Dentista\n0 - Sair\n\nEscolha uma opção: ")

    if i == "1":
        try:
            subprocess.run(['python', program_to_run] + ["frontDesk"], check=True)
        except:
            try:
                subprocess.run(['python3', program_to_run] + ["frontDesk"], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Erro ao executar 'dentist': {e.returncode}")
            except FileNotFoundError:
                print(f"Arquivo '{program_to_run}' não encontrado.")
            except Exception as e:
                print(f"Ocorreu um erro: {e}")
    elif i == "2":
        try:
            subprocess.run(['python', program_to_run] + ["frontDesk"], check=True)
        except:
            try:
                subprocess.run(['python3', program_to_run] + ["dentist"], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Erro ao executar 'dentist': {e.returncode}")
            except FileNotFoundError:
                print(f"Arquivo '{program_to_run}' não encontrado.")
            except Exception as e:
                print(f"Ocorreu um erro: {e}")

    elif i == "0":
        start = False

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nOpção inválida! Por favor, tente novamente com as opções fornecidas\n")


