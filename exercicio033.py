# Crie um fluxo para decidir se uma pessoa pode votar (idade >= 16).

def autentica_vot(idade):
    if not isinstance(idade, int):
        return None
    return True if idade >=16 else False

entrada_idade = 20

status_vot = autentica_vot(entrada_idade)
print(f"Status votação: {status_vot}")