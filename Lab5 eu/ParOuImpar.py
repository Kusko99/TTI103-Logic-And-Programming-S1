#entrada
numero = int(input("Digite o número para descobrir se ele é par ou ímpar: "))
#estrutura de decição
if (numero%2 == 0):
    print(f'O número {numero} é par')
elif (numero%2 != 0):
    print(f'O número {numero} é ímpar')
else:
    print('Não é um valor válido')