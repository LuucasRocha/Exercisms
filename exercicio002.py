# Exercício 002 - Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o
#valor da compra for menor que R$ 20,00; caso contrário, o lucro será de 30%.
#Elabore um algoritmo que leia o valor do produto e imprima o valor de venda para
#o produto.

def gera_valor(n):
    if n < 20:
        lucro = n * 0.45
    else:
        lucro = n * 0.30
    return n + lucro 
    
print(gera_valor(10))