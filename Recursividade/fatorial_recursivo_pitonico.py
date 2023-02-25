import time

def fatorial_recursivo(valor):
    if valor == 0 or valor == 1:
        return 1
    else :
        return valor * fatorial_recursivo(valor-1)

inicio = time.time()
print(fatorial_recursivo(35))
fim = time.time()
print(f'Demorou: {fim-inicio}')