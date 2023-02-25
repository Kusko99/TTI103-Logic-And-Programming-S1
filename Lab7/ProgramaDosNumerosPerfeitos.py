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

tempos,perfeitos = [], []
numero = int(input("Digite o número inteiro Positivo: "))
for num in range (1, numero + 1):
    divisores, tempo = acha_divisores(num)
    if sum(divisores[:-1]) == num:
        perfeitos.append(num)
    tempos.append(tempo)
print(f'Lista com os números perfeitos entre 1 e {numero}:\n{perfeitos}')
print(f'Tempo de execução de busca: {sum(tempos):.4f} segundos')
