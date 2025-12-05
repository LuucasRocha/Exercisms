# Crie um fluxo para decidir se uma pessoa pode votar (idade >= 16).

def valida_votacao(idade):
    if not isinstance(idade, int):
        return None
    return True if idade >= 16 else False

entrada = 21

print(f"{valida_votacao(entrada)}")