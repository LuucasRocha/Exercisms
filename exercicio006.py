#Criar um programa que encontre todos os números primos em um intervalo definido pelo usuário.

def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False   
            break
    else:
        return True
    
intervalo_inicial = int(input("Digite o valor inicial do intervalo: "))
intervalo_final =  int(input("Digite o valor final do intervalo: "))

lista_primos = []

for num in range(intervalo_inicial, intervalo_final + 1):
    if eh_primo(num):
        lista_primos.append(num)

print(lista_primos)

