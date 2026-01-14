listaNumeros = list()

for i in range(5):
    numero = int(input(f"Digite um valor para a Posição {i}: "))
    listaNumeros.append(numero)
    
print("=-"*30)
print(f"Você digitou os valores {listaNumeros}")
print(f"O maior valor digitado foi {max(listaNumeros)} nas posições ")
print(f"O menor valor digitado foi {min(listaNumeros)} nas posições ")
