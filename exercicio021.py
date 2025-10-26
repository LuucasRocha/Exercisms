#Crie uma função soma_pares(lista) que receba uma lista de números e retorne a soma somente dos pares

def soma_pares(lista):
   return sum(num for num in lista if num % 2 == 0) 
    
lista = [1,2,3,4,5,6,7]
print(soma_pares(lista))