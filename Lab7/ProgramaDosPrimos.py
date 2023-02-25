import time

#modularização
def acha_divisores(numero):
    diviosores = []
    inicio = time.time()
    for something in range (1,int(numero**0.5)+1):
        if numero%something == 0:
            diviosores.append(something)
            if numero//something != something:
                diviosores.append(numero//something)
    diviosores.sort()
    fim = time.time()
    tempo = fim - inicio
    return diviosores, tempo

tempos,primos = [], [1]
numero = int(input("Digite o número inteiro Positivo: "))
if numero != 2:
    for num in range (3, numero + 1, 2):
        divisores, tempo = acha_divisores(num)
        if len(divisores) == 2:
            primos.append(num)
        tempos.append(tempo)
else:
    primos.append(2)
print(f'Lista com os números primos entre 1 e {numero}:\n{primos}')
print(f'Tempo de execução de busca: {sum(tempos):.4f} segundos')
