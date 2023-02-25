#entrada
Produto_1 = int(input('Digite o valor do produto 1: '))
Produto_2 = int(input('Digite o valor do produto 2: '))
Produto_3 = int(input('Digite o valor do produto 3: '))
#processamento
imposto = 7 / 100
total_compra = Produto_1 + Produto_2 + Produto_3
total_imposto = (Produto_1*imposto)+(Produto_2*imposto)+(Produto_3*imposto)
total_compra_com_imposto = total_compra + total_imposto
#saída
print('O total da compra sem impostos é: ', total_compra)
print('O total de imposto a pagar é: ', total_imposto)
print('O total da compra com imposto será: ',total_compra_com_imposto)