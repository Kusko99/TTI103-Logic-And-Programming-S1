n = int(input("Digite o tamanho da sequência: "))
sequencia = []
crescimento = 0
crescimentos = []
for i in range(n):
    numero = int(input("Digite: "))
    sequencia.append(numero)
for i in range(len(sequencia)):
    if sequencia[i-1] < sequencia[i]:
        crescimento += 1
    elif sequencia[i-1] > sequencia[i]:
        crescimentos.append(crescimento)
        crescimento = 0
crescimentos.append(crescimento)
print(max(crescimentos))