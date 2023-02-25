def Entrada ():
    num = input("Digite um número: ")
    x = input("Qual algarismo você quer saber: ")
    lista = list(num)
    return lista,x

def NumAlgorismos (lista,x):
    if len(lista) == 0:
        return 0
    else:
        y = lista.pop(0)
        if y == x:
            contador = 1
        else:
            contador = 0
        return contador + NumAlgorismos(lista,x)

lista,x = Entrada()
print(NumAlgorismos(lista,x))
