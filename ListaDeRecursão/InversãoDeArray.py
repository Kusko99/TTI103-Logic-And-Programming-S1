def entrada (texto):
    array = []
    n = int(input("Quantos elementos : "))
    for _ in range(n):
        x = int(input(texto))
        array.append(x)
    return array  

def Inversao (array):
    if len(array) == 1:
        return array[0]
    else:
        array[0],array[-1] = array[-1],array[0]
        Inversao(array[1:-2])
        return array

array = entrada("Digite um inteiro: ")
print(Inversao(array))
