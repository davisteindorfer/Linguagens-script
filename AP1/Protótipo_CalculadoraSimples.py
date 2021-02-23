a = True
while a == True:
  Operação = []
  x = float(input("Entre um número \n"))
  while isinstance(x,float) == False:
    print("Entrada inválida")
    x = float(input("Entre um número \n"))
  Operação.append(x)

  op = str(input("Entre uma operação (+ - * /) \n"))
  while isinstance(op,str) == False:
    print("Entrada inválida")
    op = str(input("Entre uma operação (+ - * /) \n"))
  Operação.append(op)

  y = float(input("Entre um número \n"))
  while isinstance(y,float) == False:
    print("Entrada inválida")
    y = float(input("Entre um número \n"))
  Operação.append(y)

  for i in range(0,3):
    if Operação[i] == "+":
      print(Operação[i-1],"+",Operação[i+1],"=", Operação[i-1]+Operação[i+1])
    if Operação[i] == "-":
      print(Operação[i-1],"-",Operação[i+1],"=", Operação[i-1]-Operação[i+1])
    if Operação[i] == "*":
      print(Operação[i-1],"*",Operação[i+1],"=", Operação[i-1]*Operação[i+1])
    if Operação[i] == "/":
      print(Operação[i-1],"/",Operação[i+1],"=", Operação[i-1]/Operação[i+1])  
  print("Se deseja fazer outra operação entre o numero 1")
  print("caso contrário entre qualquer numero")
  t = int(input())
  if t != 1:
    a = False
