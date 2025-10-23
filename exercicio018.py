# Criar um programa que faça um pequeno dicionário com as seguintes informações: nome, idade, cidade.
usuario = {
    "nome": input("Digite seu nome: "),
    "idade": int(input("Digite sua idade: ")),
    "cidade": input("Digite sua cidade: ")
}

print("Dicionário criado:")
print(usuario)