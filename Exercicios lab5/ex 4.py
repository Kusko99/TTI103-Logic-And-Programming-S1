#importações
import random

#entrada
print('Digite (M) se você gostaria de multiplicar e (S) se você gostaria de somar')
x = (input('Digite a função que deseja: '))
x = x.lower()  

#estrutura de decição
if x == 'm':
    y = random.randint(0, 100)
    z = random.randint(0, 100)
    x = y*z
    print(f'{y} * {z} = {x}')
elif x== 's':
    y = random.randint(0, 100)
    z = random.randint(0, 100)
    x = y+z
    print(f'{y} + {z} = {x}')
else:
    print('Não é um comando válido')