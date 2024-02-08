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
