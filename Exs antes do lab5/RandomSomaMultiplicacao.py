#importações
import random
#entrada
print('''Esse programa calcula uma soma ou multiplicação para um número aletório
Digite (S) para fazer a soma 
Digite (M) para fazer a multiplicação''')
comando = False
while not (comando):
    try:
        entrada = input('Digite o seu comando: ')
        if entrada == 'S' or 'M':
                comando = True
        elif entrada == 's' or 'm':
            print('Digite em letra maiusculas')
        else:
                print("Digite um comando válido")
        except ValueError: 
            print('Oi')
#processamento
if comando == 'S':
    x = random.randint(0,100)
    y = random.randint(0,100)
    z = (x+y)
    print(f'A sua soma de {x:,.2f} + {y:,.2f} é igual a {z:,.2f}')
elif comando == 'M':
    x = random.randint(0,100)
    y = random.randint(0,100)
    z = (x*y)
    print(f'A sua multiplicação de {x:,.2f} vezes {y:,.2f} é igual a {z:,.2f}')
else:
    print('Deu muita merda')

