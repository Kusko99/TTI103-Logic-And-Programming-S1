valor = float(input())
valor = int(valor*100)
notas = [10000, 5000, 2000, 1000, 500, 200]
print('NOTAS: ')
for nota in notas:
    quant_notas = valor//nota
    valor = valor%nota
    print(f'{quant_notas} nota(s) de R$ {nota/100:.2f}')
moedas = [100,50,25,10,5,1]
print('MOEDAS: ')
for moeda in moedas:
    quant_moedas = valor//moeda
    valor = valor % moeda
    print(f'{quant_moedas} moeda(s) de R$ {moeda/100:.2f}')
