def entrada(texto):
    x = int(input(texto))
    return x

def fibonnaci(num):
    if num <= 1:
        return num
    else:
        return fibonnaci(num -1) + fibonnaci(num -2)

num = entrada("Digite o número para dscobrir o fibonnaci: ")
print(f'O fibonnaci de {num} é {fibonnaci(num)}')