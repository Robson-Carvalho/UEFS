class Entrevistado:
  def __init__(self, nome, idade, sexo, quantidade_filhos, salario):
    self.nome = nome
    self.idade = idade
    self.sexo = sexo
    self. quantidade_filhos =  quantidade_filhos
    self.salario = salario
  
entrevistados = {}

i = 5
for i in range(0, i):
  nome = input("Digite o nome: ")
  idade = int(input("Digite a idade: "))

  op_sexo = input("Digite (F) Feminino ou (M) Masculino: ")

  sexo = ""

  if op_sexo == "F" or op_sexo == "f":
    sexo = "F"
  elif op_sexo == "M" or op_sexo == "m":
    sexo = "M"
  else:
    sexo = "F"

  quantidade_filhos = int(input("Digite a quantidade d filhos: "))

  salario = float(input("Digite o salário: "))

  entrevistado = Entrevistado(nome, idade, sexo, quantidade_filhos, salario)

  entrevistados[i] = entrevistado

  print("\n")

def calcularMediaSalarial(entrevistados):
  salarios = 0
  contador = 0
  for index in entrevistados:
    salarios += entrevistados[index].salario
    contador += 1

  media = salario / contador

  print(f"A média salarial é R$ {media}\n")

def sexoMaiorSalario(entrevistados):
  maiorSalarioHomem = 0
  maiorSalarioMulher = 0

  for index in entrevistados:
    if entrevistados[index].sexo == "M":
      if maiorSalarioHomem < entrevistados[index].salario:
        maiorSalarioHomem = entrevistados[index].salario
    else:
      if maiorSalarioMulher < entrevistados[index].salario:
        maiorSalarioMulher = entrevistados[index].salario

  print(f"\nO maior salario do sexo masculino é {maiorSalarioHomem}\nE o maior salário do sexo feminino é {maiorSalarioMulher}\n")

def filtrarBaixaRenda(entrevistados):
  quantidade = 0
  for index in entrevistados:
    if entrevistados[index].salario < 1000 and entrevistados[index].idade < 30 and entrevistados[index].quantidade_filhos > 5:
      quantidade += 1

  print(f"\nA quantidade de pessoas com saláril abaixo de 1000 reais, abaixo de 30 anos e com 5 ou mais filhos é {quantidade}\n")

def filtrarMulheresComFilhos(entrevistados):
  quantidadeMulheresComFilho = 0
  quantidadePessoas = 0

  for index in entrevistados:
      quantidadePessoas += 1
      if entrevistados[index].quantidade_filhos >= 1:
        quantidadeMulheresComFilho += 1

  porcentagem = (quantidadeMulheresComFilho / quantidadePessoas) * 100

  print(f"\nA porcentagem de mulheres com filhos é {porcentagem}%")
      
calcularMediaSalarial(entrevistados)
sexoMaiorSalario(entrevistados)
filtrarBaixaRenda(entrevistados)
filtrarMulheresComFilhos(entrevistados)
