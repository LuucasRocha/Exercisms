def cont_vogais(palavra):
    vogais = "aáãÂéêeiíîóôoúûuAEIOU"
    contadorVogais = ""
    
    for letra in palavra:
        if letra.lower() in vogais:
            contadorVogais += letra
    
    return contadorVogais

print(cont_vogais("Paralelepípedo"))
    

