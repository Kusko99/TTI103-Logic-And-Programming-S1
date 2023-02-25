N = int(input('Digite o numero de canetas compradas: '))
Z = float(input('Digite o quando você pagou: '))
Y = float(input('Digite o quando você recebeu de troco: '))
X = (Z-Y)/N
print(f'Cada caneta comprada custou:{X:,.2f}')