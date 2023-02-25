def Multi_Rec(x,y):
    if x == 0 or y == 0:
        return 0
    resultado = y + Multi_Rec(x-1,y)
    return resultado

def Entrada():
    x = int(input("Digite x: "))
    y = int(input("Digite y: "))
    return x, y
x,y = Entrada()
print(Multi_Rec(x,y))