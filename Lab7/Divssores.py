import time
lista = []
inicio = time.time()
numero = int(input("Digite um número: "))
for something in range (1,int(numero**0.5)+1):
    if numero%something == 0:
        lista.append(something)
        if numero//something != something:
            lista.append(numero//something)
lista.sort()
print(f'Lista com os divisores de {numero}: \n{lista}')
fim = time.time()
tempo = fim - inicio
print(f'Tempo de execução: {tempo:,.4f} segundos.')