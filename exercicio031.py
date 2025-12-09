#Crie um programa que realize o preenchimento de uma lista com 10 caracteres e, em seguida, imprima na tela apenas as vogais presentes no vetor.

def lista_vogais(lista):
    vogais = "aeiou"
    vogais_lista = []
    for i in lista:
        if i in vogais:
            vogais_lista.append(i)
    return vogais_lista

print(lista_vogais(["a", "b", "c", "d", "!", "e", "i", "o"]))

