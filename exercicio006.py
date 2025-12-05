#Criar um programa que encontre todos os números primos em um intervalo definido pelo usuário.

def imprime_primos(n1, n2):
    lista_primos = []
    for num in range(n1, n2 + 1):
        if num > 1:
            eh_primo = True
            for i in range(2, int(num**0.5) + 1):
                if num % i:
                    eh_primo = False
            if eh_primo:
                lista_primos.append(num)
    return lista_primos

print(imprime_primos())


