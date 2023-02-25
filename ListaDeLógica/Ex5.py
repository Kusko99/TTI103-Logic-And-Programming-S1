binario = int(input("Digite o seu código binário composto de zeros e uns: "))
bit = []
numero = 0
while binario != 0:
    bit.append(binario%10)
    binario = binario//10
print(bit)
for i in range(0,len(bit),1):
    numero = numero+bit[i]*(2**i)
print(numero)
