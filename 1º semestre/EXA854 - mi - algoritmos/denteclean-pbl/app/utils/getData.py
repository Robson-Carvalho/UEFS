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

  start = True
  while start:
    try:
      anoAtual = datetime.now().year
      year = int(input("Digite o número do ano: "))
      if 2000 <= year <= anoAtual:
          start = False
      else:
          print(f"\nO número deve estar entre 2000 e {anoAtual}. Tente novamente.\n")
    except ValueError:
      print("\nValor inválido! Por favor, digite um número válido.\n")

  return f"{day:02d}/{month:02d}/{year:02d}"

"""
Autor: Robson Carvalho de Souza

Componente Curricular: EXA 854-MI-Algoritmos

Concluido em: 08/02/2024

Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
"""
