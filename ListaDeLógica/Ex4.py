numero = int(input("Digite o numero: "))
algarismo = []
while numero != 0:
    algarismo.append(numero%10)
    numero = numero//10
for i in range(len(algarismo)-1,-1,-1):
    print(algarismo[i])