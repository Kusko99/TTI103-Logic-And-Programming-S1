def entrada(texto):
    x = int(input(texto))
    return x

def elevar(x,n):
    if n == 1:
        return x
    else:
        resultado = 0
        for _ in range(n):
            resultado = x * (elevar(x,n-1))
        return resultado
x = entrada("Digite x: ")
n = entrada("Digite n: ")
print(f"O resultado é :{elevar(x,n)} ")