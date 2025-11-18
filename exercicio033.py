# Crie um fluxo para decidir se uma pessoa pode votar (idade >= 16).

def autentica_votacao(idade):
    return True if idade >=16 else False

while True:
    nome = input("Digite seu nome: ")

    try:
        idade = int(input("Digite sua idade: "))

        verifica_vot = autentica_votacao(idade)
        if verifica_vot:
            print(f"Eleitor: {nome} \nStatus Votação: Ok")
        else:
            print(f"Eleitor: {nome} \nStatus Votação: Negado")

    except ValueError:
        print("Idade inválida, digite um número.")