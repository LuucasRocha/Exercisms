'''
Peça 10 números ao usuário e mostre:

maior valor

menor valor

média

lista ordenada

quantidade de números pares
'''

def maior_valor(lista):
  maior = lista[0]
  for num in lista:
    if num > maior:
      maior = num
  return maior

def menor_valor(lista):
  menor = lista[0]
  for num in lista:
    if num < menor:
      menor = num
  return menor

def media_valores(lista): # sem usar sum e len 
  soma = 0
  cont = 0
  for num in lista:
    soma += num
    cont += 1
  return soma / cont

def ordenar_numeros(lista):
  return sorted(lista)

def quantidade_pares(lista):
  cont = 0
  for num in lista:
    if num % 2 == 0:
      cont += 1
  return cont

try:
  lista_entrada = []
  for i in range(1, 11):
    entrada = int(input(f"Digite o {i}º número: "))
    lista_entrada.append(entrada)
  
  print("-------------Programa iniciado---------------")
  print(f"Maior valor: {maior_valor(lista_entrada)}")
  print(f"Menor valor: {menor_valor(lista_entrada)}")
  print(f"Média dos valores: {media_valores(lista_entrada)}")
  print(f"Números ordenados: {ordenar_numeros(lista_entrada)}")
  print(f"Quantidade de números pares : {quantidade_pares(lista_entrada)}")

except ValueError:
  print("Erro! Entrada inválida. Digite uma lista de números.")

  
