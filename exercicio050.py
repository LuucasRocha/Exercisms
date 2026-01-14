palavras = ['aprender','jogar', 'lucas', 'amanda']

for palavra in palavras:
    print(f"\nNa palavra {palavra.upper()} temos ", end='')
    vogais = 'aeiou'
    for letra in palavra:
        if letra.lower() in vogais:
            print(letra, end=' ')
        