lista_numeros = []

while True:
  try:
    entrada = int(input("Digite um número: (Ou 0 para encerrar o programa)"))
    if entrada == 0:
        break
    lista_numeros.append(entrada)
  
  except ValueError:
      print("Entrada inválida! Digite apenas números inteiros.")
 
print("----- Programa encerrado -----")   
print(f"A soma total dos números é: {sum(lista_numeros)}")
print(f"A quantidade de números total é: {len(lista_numeros)}")
print(f"A média dos números é: {sum(lista_numeros) / len(lista_numeros)}")