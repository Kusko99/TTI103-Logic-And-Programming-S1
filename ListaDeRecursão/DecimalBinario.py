def Entrada (texto):
    num = int(input(texto))
    return num

def DecimalParaBinario (num):
    if num > 1:
        DecimalParaBinario(num//2)
        print(num%2,end = '')


num = Entrada("Digite um número: ")
print(DecimalParaBinario(num))