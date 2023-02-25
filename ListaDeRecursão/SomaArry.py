def entrada (texto):
    array = []
    n = int(input("Quantos elementos : "))
    for _ in range(n):
        x = float(input(texto))
        array.append(x)
    return array    

def SomaDeReais (array):
    if len(array) == 1:
        return array[0]
    else:
        return array[0] + SomaDeReais(array[1:])

array = entrada("Digite um número real")
print(SomaDeReais(array))