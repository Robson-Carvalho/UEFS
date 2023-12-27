import subprocess

program_to_run = './app/main.py'
arguments = ['dentist']

try:
    subprocess.run(['python', program_to_run] + arguments, check=True)
except subprocess.CalledProcessError as e:
    print(f"Erro ao executar 'dentist': {e.returncode}")
except FileNotFoundError:
    print(f"Arquivo '{program_to_run}' não encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
