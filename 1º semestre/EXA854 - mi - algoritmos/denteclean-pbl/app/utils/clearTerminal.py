import os

def clearTerminal():
  input("Pressione Enter para continuar!")
  os.system('cls' if os.name == 'nt' else 'clear')
