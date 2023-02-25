#entrada
preco_original = float(input('Digite o preço original do produto: '))
Desconto = 0.20
#processamento
preco_final = preco_original - (preco_original * Desconto)
#saída
print(f'O valor final do produto será: {preco_final:.2f}')
