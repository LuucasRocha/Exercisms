# Peça ao usuário uma palavra e mostre quantas vogais ela contém.
def cont_vogais(palavra):
    soma_vogais = sum(1 for i in palavra if i in "aeiouAEIOU")
    return f"A palavra contém {soma_vogais} vogais."

print(cont_vogais(""))