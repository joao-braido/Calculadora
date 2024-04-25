def add(x,y): #criar função de adição
  return x + y

def sub (x, y): #criar função de subtração
  return x - y

def mult (x, y ): #criar função de multiplição
  return x * y

def div (x,y): #criar função de divisão
  return x / y

#calculadora
print("Operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

while True:
  escolha = input("Escolha um número: 1/2/3/4: ")
  
  if escolha in ('1', '2', '3', '4'):
    num1 = float(input("Primeiro Número: "))
    num2 = float(input("Segundo Número: "))

    if escolha == '1':
      print(num1, "+", num2, "=", add(num1, num2))
             
    elif escolha == '2':
      print(num1, "-", num2, "=", sub(num1, num2))

    elif escolha == '3':
      print(num1, "*", num2, "=", mult(num1, num2))

    elif escolha == '4':
      print(num1, "/", num2, "=", div(num1, num2))
    else:
      print("Número inválido!")

