"""Frequência de letras.
Peça uma frase e conte quantas vezes cada letra aparece."""

frase = input("Digite uma frase: ").lower()
frequencia = {}

for letra in frase:
    if letra.isalpha():
        if letra in frequencia:
            frequencia[letra] += 1
        else:
            frequencia[letra] = 1

for letra, contagem in frequencia.items():
    print(f"A letra '{letra}' aparece {contagem} vezes.")
    
    