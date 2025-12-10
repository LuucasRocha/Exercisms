#Peça um número n e faça uma contagem regressiva até 0.

def contagem(n):
    for i in range(n, -1, -1):
        print(i)
        
print(contagem(4))
    