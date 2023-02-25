import re


x = float(input("Digite o valor a ser elevado: "))
n = int(input("Digite a potência: "))
resultado = x
for i in range(n-1):
    resultado = resultado*x
print(resultado)