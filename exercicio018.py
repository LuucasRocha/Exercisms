# Criar um programa que faça um pequeno dicionário com as seguintes informações: nome, idade, cidade.

usuario = {
    "nome": input("Digite seu nome: "),
    "idade": int(input("Digite sua idade: ")),
    "cidade": input("Digite o nome da sua cidade: ")
}

print("As informações do usuário são:")
for chave, valor in usuario.items():
    print(f"{chave.capitalize()}: {valor}")