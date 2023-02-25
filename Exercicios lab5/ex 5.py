print('''Digite o pagamento de sua preferência:
(1)para pagamento À vista(PIX,dinheiro ou cheque)
(2)para pagamento À vista(Crédito)
(3)para pagamento 2 parcelas (Crédito)
(4)para pagamento 3 ou mais parcelas(Crédito)''')
x = int(input('Digite a forma de pagamento: '))
PRODUTO = float(input('Digite o valor do produto: '))

#estrutura de decisão
if x == 1:
    DESCONTO = PRODUTO*0.1
    PRODUTO = PRODUTO - DESCONTO
    print(f'O valor a ser pago será {PRODUTO:,.2f}')    
elif x == 2:
    DESCONTO = PRODUTO*0.05
    PRODUTO = PRODUTO - DESCONTO
    print(f'O valor a ser pago será {PRODUTO:,.2f}')
elif x == 3:
    PRODUTO_F = PRODUTO/2
    print(f'O valor a ser pago será {PRODUTO:,.2f},em duas parcelas de {PRODUTO_F:,.2f}')
elif x == 4:
     JUROS = PRODUTO*0.2*3
     PRODUTO = PRODUTO + JUROS
     PRODUTO_F = PRODUTO/3
     print(f'O valor a ser pago será {PRODUTO:,.2f}, em três parcelas de {PRODUTO_F:,.2f}')
else:
    print('Não é um comando válido')