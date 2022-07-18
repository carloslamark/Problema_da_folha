valorCorreto = {'1':["carlos", 1300], '2':["rr", 1400]}
valorEmpresa = {'1':["carlos", 1200], '2':["rr", 1500]}
f = int(-1)

def leituraValorCorreto(valorCorreto):
  print("Id Colaborador: ")
  id = input()
  aux = [" ", 0]
  print("Nome Colaborador: ")
  aux[0] = input()
  print("Salário Colaborador: ")
  aux[1] = float(input())
  valorCorreto[id] = aux

def leituraEmpresa(valorEmpresa):
  print("Id Colaborador: ")
  id = input()
  aux = [" ", 0]
  valorEmpresa[id] = []
  print("Nome Colaborador: ")
  aux[0] = input()
  print("Salário Colaborador: ")
  aux[1] = float(input())
  valorEmpresa[id] = aux

def relatorio(valorCorreto, valorEmpresa):
  #Colaboradores com salarios diferentes
  print("Colaboradores com o salário errado:\n")
  for id in valorCorreto:
    dif = valorCorreto[id][1] - valorEmpresa[id][1]
    if dif>0:
      print("- ", valorCorreto[id][0], " está R$", float(dif), " abaixo do valor correto.\n")
    elif dif<0:
      dif *= -1
      print("- ", valorCorreto[id][0], " está R$", float(dif), " acima do valor correto.\n")

  somaDif = float(0)
  cont = 0
  for i in valorCorreto:
    aux = float(valorCorreto[id][1] - valorEmpresa[id][1])
    if aux<0:
      aux *= -1
    somaDif += aux
    cont += 1
  print("Diferença total: ", float(somaDif), "\n")
  print("Diferença média: ", float(somaDif/float(cont)))
  print("\n\n")



while(f):
  print("1 Ler Valor Correto\n")
  print("2 Ler Valor Empresa\n")
  print("3 Gerar Relatório\n")
  f = int(input())
  if f == 1:
    leituraValorCorreto(valorCorreto)
  elif f == 2:
    leituraEmpresa(valorEmpresa)
  elif f == 3:
    relatorio(valorCorreto, valorEmpresa)
