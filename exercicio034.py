#Tipo de triangulo

def triangulo(num1, num2, num3):
  if (num1 < num2 + num3) and (num2 < num1 + num3) and (num3 < num1 + num2):
    if num1 == num2 == num3:
      return "É um triângulo Equilátero."
    elif (num1 == num2) or (num1 == num3) or (num2 == num3):
      return "É um triângulo Isósceles."
    else:
      return "É um triângulo Escaleno."
  else:
    return "Os valores não formam um triângulo."

try:
  entrada1 = float(input("Digite o primeiro número: "))
  entrada2 = float(input("Digite o segundo número: "))
  entrada3 = float(input("Digite o terceiro número: "))

  print(triangulo(entrada1, entrada2, entrada3))

except ValueError:
  print("Erro: Entrada inválida.")