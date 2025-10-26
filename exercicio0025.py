#Crie uma função conta_vogais(texto) que receba uma string e retorne quantas vogais (a, e, i, o, u) ela contém.
'''
def cont_vogais(texto):
    vogais = "aeiou"
    cont = 0
    for letra in texto.lower():
        if letra in vogais:
            cont += 1
    return cont

contagem = cont_vogais("Vamos nessa!")
print(contagem)
'''

def cont_vogais(texto):
    return sum(1 for letra in texto.lower() if letra in "aeiouáéíóúãõâêîôû")

contagem = cont_vogais("Vamos ver essa agóra!")
print(contagem)