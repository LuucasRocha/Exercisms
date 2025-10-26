# Exercício 002 - Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o
#valor da compra for menor que R$ 20,00; caso contrário, o lucro será de 30%.
#Elabore um algoritmo que leia o valor do produto e imprima o valor de venda para
#o produto.

valor_compra = float(input("Digite o valor de compra do produto: R$ "))

if valor_compra < 20.0:
    lucro = 0.45
else:
    lucro = 0.30

valor_venda = valor_compra * (1 + lucro)
print(f"O valor de venda para o produto é: R$ {valor_venda:.2f}")


