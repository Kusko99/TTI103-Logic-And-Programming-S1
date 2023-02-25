comprimentos = []
for cont in range (3):
    tipo_ok = False
    pos_ok = False
    while not (tipo_ok and pos_ok):
        try:
            comp = float(input(f'Digite o comprimeto #{cont+1}:'))
            tipo_ok = True
            if comp <= 0:
                print('ERRo: O comprimento deve ser positivo!')
            else:
                pos_ok = True
        except ValueError: 
            print('ERRO: O comprimento deve ser um número real!!!')
        comprimentos.append(comp)
print(comprimentos)
#===================================================================
#verificação da existência e tipo do triângulo
#======================================================================
a,b,c = comprimentos[0], comprimentos[1], comprimentos[2]
#========================================================================
#teste
#=======================================================================
Teste_a = (abs(b-c)<a) and (a<(b+c))
Teste_b = (abs(a-c)<b) and (b<(a+c))
Teste_c = (abs(a-b)<c) and (c<(a+b))
if Teste_a and Teste_b and Teste_c:
   #É um triângulo!
   if(a==b)and(b==c):
       tring = "equilátero"
   elif (a==b) or (a==c) or (b==c):
       tring = "isósceles"
   else:
       trig = 'escaleno'
       print(f'\nO triângulo formado é do tipo {trig}.')
else: 
    #não é possível construir um triângulo
    print('\nNão é possível construir um triângulo com esse Lados.')
    