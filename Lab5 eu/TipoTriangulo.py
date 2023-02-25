comprimentos = []
for cont in range(3):
    tipo_ok = False
    pos_ok = False
    while not tipo_ok and pos_ok:
        try: 
            comp = float(input(f'Digite o comprimento #{cont+1}:'))
            tipo_ok = True
            if comp <= 0:
                print('O comprimento deve ser um número positivo')
            else:
                pos_ok = True
        except ValueError:
            print('Erro: o comprimento deve ser um número real')
        comprimentos.append(comp)
a,b,c = comprimentos[0], comprimentos[1], comprimentos[2]
teste_a = (abs(b-c)<a) and (a<(b+c))
teste_b =(abs(a-c)<b) and (b<(a+c))
teste_c =(abs(a-b)<c) and (c<(a+b))
if teste_a and teste_b and teste_c:
    #é um triângulo
    if (a==c) and (b==c):
        print('O triângulo é equilátero')
    elif(a==b) or (a==c) or (b==c):
        print('O triângulo é Isósceles')
    else:
        print('O triângulo é escaleno')
else:
    print('Não é triângulo')