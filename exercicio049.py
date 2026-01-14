lista_numeros = list()
for i in range(4):
    num = int(input(f"Digite o {i + 1}º número inteiro: "))
    lista_numeros.append(num)
    
print(lista_numeros)

if 9 in lista_numeros:
    print(f"O valor 9 apareceu {lista_numeros.count(9)} vezes.")
else:
    print("O valor 9 não consta na lista.")

if 3 in lista_numeros:
    print(f"O valor 3 está ná {lista_numeros.index(3) + 1}º posição.")
else:
    print("O valor 9 não consta na lista")

print("Os valores pares são:", end=' ')
for num in lista_numeros:
    if num % 2 == 0:
        print(num, end=' ')

        
