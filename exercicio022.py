#Exercicio do maior número.

def eh_maior(n1, n2):
    if n1 > n2:
        return f"{n1} é maior que {n2}."
    elif n2 > n1:
        return f"{n2} é maior que {n1}"
    else:
        return "Os números são iguais."
    
entrada1 = int(input("Digite o primeiro número: "))
entrada2 = int(input("Digite o segundo número: "))

print(eh_maior(entrada1, entrada2))



