#Implemente eh_palindromo(texto) que retorna True se texto for palíndromo ignorando espaços, pontuação e diferenças de maiúsculas/minúsculas.

def eh_palindromo(texto):
    texto = texto.lower().strip()
    texto_limpo = "".join(c for c in texto if c.isalnum())
    return texto_limpo == texto_limpo[::-1]
    
entrada = input("Digite um texto: ")
verifica_palindromo = eh_palindromo(entrada)

print(f"\n Resultado: {verifica_palindromo}")