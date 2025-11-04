#Crie um programa que realize o preenchimento de uma lista com 10 caracteres e, em seguida, imprima na tela apenas as vogais presentes no vetor.

while True:
    entrada = input("Digite uma lista composta por 10 caracteres, separados por vírgula: ")
    lista_entrada = [x.strip() for x in entrada.split(",")]  # Remove espaços em branco
    
    if len(lista_entrada) != 10:
        print("A lista deve possuir exatamente 10 caracteres. Tente novamente.")
    else:
        break

# Filtrar apenas as vogais (considerando apenas minúsculas, como no código original)
vogais = "aeiou"
entrada_vogais = [i for i in lista_entrada if i in vogais]

# Imprimir as vogais
print("Vogais presentes na lista:", entrada_vogais)

        

