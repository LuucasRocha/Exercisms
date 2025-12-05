# Crie um fluxo para decidir se uma pessoa pode votar (idade >= 16).

def verifica_idade_voto(idade):
    if not isinstance(idade, int):
        return None
    return True if idade >= 16 else False

entrada = 16

print(verifica_idade_voto(entrada))