from datetime import datetime

def getSchedule():
  start = True
  while start:
      try:
          hour = int(input("\nDigite a hora (0-23): "))
          if 0 <= hour <= 23:
              start = False
          else:
              print("\nA hora deve estar entre 0 e 23. Tente novamente.\n")
      except ValueError:
          print("\nValor inválido! Por favor, digite um número válido.\n")

  start = True
  while start:
      try:
          minute = int(input("Digite os minutos (0-59): "))
          if 0 <= minute <= 59:
              start = False
          else:
              print("\nOs minutos devem estar entre 0 e 59. Tente novamente.\n")
      except ValueError:
          print("\nValor inválido! Por favor, digite um número válido.\n")

  return f"{hour:02d}:{minute:02d}:{0:02d}"

