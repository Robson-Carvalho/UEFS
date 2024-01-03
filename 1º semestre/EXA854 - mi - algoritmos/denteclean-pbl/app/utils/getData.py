from datetime import datetime

def getData():
  start = True
  while start:
    try:
      day = int(input("Digite o número do dia: "))
      if 1 <= day <= 31:
          start = False
      else:
          print("\nO número deve estar entre 1 e 31. Tente novamente.\n")
    except ValueError:
      print("\nValor inválido! Por favor, digite um número válido.\n")

  start = True
  while start:
    try:
      month = int(input("Digite o número do mês: "))
      if 1 <= month <= 12:
          start = False
      else:
          print("\nO número deve estar entre 1 e 12. Tente novamente.\n")
    except ValueError:
      print("\nValor inválido! Por favor, digite um número válido.\n")

  return f"{day:02d}/{month:02d}/{datetime.now().year}"