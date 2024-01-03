import os

def clearTerminal():
  input("\nPressione Enter para continuar!")
  os.system('cls' if os.name == 'nt' else 'clear')
