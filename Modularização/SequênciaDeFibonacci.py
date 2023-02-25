def entrada():
    entradaOk = False
    while not entradaOk:
        try:
            rangeFibonacci = int(input("Digite o range: "))
            if rangeFibonacci > 2:
                entradaOk = True
            else:
                print("Digite um númeor inteiro maior que 2")
        except:
            print("Digite um número")
    return rangeFibonacci

def soma (a,b):
    return a + b

def sequenciaFibonnaci(rangeFibonacci):
    print("Ínicio da sequência de Fibonnaci")
    a,b = 0,1
    print(f'O termo 1 é "{a}"')
    for i in range(rangeFibonacci-1):
        proximo = soma(a,b)
        print(f'O termo {i+2} é "{proximo}"')
        a = b
        b = proximo
    print(f"Fim da sequência de Fibonnaci no range {rangeFibonacci}")

def main():
    rangeFibonacci = entrada()
    sequenciaFibonnaci(rangeFibonacci)

#programa principal
main()
