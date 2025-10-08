# Peça ao usuário uma palavra e mostre quantas vogais ela contém.
def eh_volgal(palavra):
    vogais = ("aeiou")
    cont = 0
    for i in palavra:
        if i in vogais:
            cont += 1
    return cont


palavra = input("Digite uma palavra: ").lower()
print(f"A palavra '{palavra}' contém {eh_volgal(palavra)} vogais.")
    