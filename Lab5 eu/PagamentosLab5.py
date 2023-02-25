print( '''Escolha o seu método de pagamento:
(1) À vista (PIX,dinheiro ou cheque): 10% de desconto
(2) À vista (Crédito): 5% de deconto
(3) 2 parcelas (Crédito): sem desconto
(4) 3 ou mais parcelas (Crédito): juros de 20%''')
metodo = input('Digite o número referente ao seu método de preferência: ')
valor = float(input("Digite o valor da compra: "))
if metodo == 1:
    desconto = valor*0.2
    valor = valor - desconto
    print(f"O preço a ser pago é {valor:,.2f}")
elif metodo == 2:
    desconto = valor*0.2
elif x == 2:
    desconto = valor*0.05
    PRODUTO = valor - DESCONTO
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
