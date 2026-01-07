'''
Implemente:
Números de 1 a 100 que são múltiplos de 3
Tabuada completa (1 a 10)
Leitura de números até o usuário digitar 0
mostre soma, quantidade e média
Cálculo de fatorial (sem biblioteca)
'''
print("Múltiplos de 3 de 1 a 100: ")
for i in range(1, 101):
    if i % 3 == 0:
        print(i)
        
for i in range(1, 11):
    print("------------------")
    print(f"Tabuada do {i}: ")
    for num in range(1, 11):
        print(f"{i} x {num} = {num * i}")
    
lista_entrada = []

while True:
    try:
        entrada = int(input("Digite um número inteiro (ou 0 para encerrar):"))
    except ValueError:
        print("Entrada inválida! Digite apenas números inteiros.")
        continue
    
    if entrada == 0:
        print("Encerrando.")
        break

    lista_entrada.append(entrada)
    
def soma_lista(lista):
    return sum(num for num in lista)

def quantidade_lista(lista):
    return sum(1 for num in lista)

def media_lista(lista):
    if len(lista) != 0:
        return sum(lista) / len(lista)
    '''
    ou com lógica pura:
    soma = 0
    quantidade = 0
    for num in lista:
        soma += num
        quantidade += 1
    return soma / quantidade
    '''

print(f"Soma da lista: {soma_lista(lista_entrada)}")
print(f"Quantidade da lista: {quantidade_lista(lista_entrada)}")
print(f"Média da lista: {media_lista(lista_entrada)}")

def fatorial(num):
    if num == 0:
        return 1
    elif num < 0:
        raise ValueError("Fatorial não definido para números negativos.")
    
    fat = 1
    for i in range(1, num + 1):
        fat = fat * i
    return fat



    


