#Peça um número n e calcule a soma de todos os números inteiros de 1 até n.

def soma_nums(n):
    return sum(num for num in range(n + 1))

print(soma_nums(5))
 