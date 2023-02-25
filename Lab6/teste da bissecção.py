#entrada de dados
print('''raiz quadrada aproximada''')
radicando = float(input('Extrair a raiz quadrada de: '))
casas_dec = int(input('Qual a precsão desejada (casas decimais)?')) 
#inicializar algoritmos
precisao = 10**(-casas_dec)
tentativas = 0
low = 0
high = max(1, radicando)
raiz = (low + high)/2
#algoritmo da bissecção
while abs(raiz**2 - radicando ) >= precisao:
    print(f'low = {low:10.10f}\thigh = {high:10.10f}')
    tentativas += 1
    if raiz**2 < radicando:
        low = raiz
    else:
        high = raiz
    raiz = (low+high)/2
#saída de dados
print(f'''\nA raiz quadrada de {radicando} é {raiz:.{casas_dec}f} dentro da precisão {precisao}.Foram necessárias {tentativas}.''')
#print(f'''\nA raiz quadrada de {radicando} é {raiz:.{casas_dec}f} dentro da precisão de {casas_dec}.Foram necessárias {tentativas}.''')
