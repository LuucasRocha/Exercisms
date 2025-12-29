# Fatorial sem usar math.factorial

def fatorial(n):
    if n < 0:
        return "Entrada inválida, número negativo"
    elif n == 0:
        return 1
    else:
        fat = 1
        for i in range(2, n + 1):
            fat *= i 
    return fat

