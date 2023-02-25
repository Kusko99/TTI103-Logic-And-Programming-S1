# Altura
altura_ok = False
tipo_altura_ok = False
while not (altura_ok and tipo_altura_ok):
    try:
        altura = float(input("Dgite a sua altura em [m]: "))
        tipo_altura_ok = True
        if altura <= 0:
            print('Erro: a altura deve ser positiva!')
        else:
            altura_ok = True
    except ValueError:
            print('Erro: A altura deve ser número real positivo!')
# Massa
massa_ok = False
tipo_massa_ok = False
while not (massa_ok and tipo_massa_ok):
    try:
        massa = float(input("Dgite a sua massa em [kg]: "))
        tipo_massa_ok = True
        if massa <= 0:
            print('Erro: a massa deve ser positiva!')
        else:
            massa_ok = True
    except ValueError:
            print('Erro: A massa deve ser número real positivo!')
#processamento
IMC = (massa/(altura**2))
#saída
if (IMC < 18.5):
    print('Você está abaixo do peso')
elif(IMC >= 18.5 and IMC < 25):
    print('Você está saudável')
elif(IMC >= 25 and IMC < 30):
    print('Você está com Peso em excesso')
elif(IMC >= 30 and IMC < 35):
    print('Você está com Obesidade Grau I')
elif(IMC >= 35 and IMC < 40):
    print('Você está com Obesidade Grau II (severa)')
else:
    print('Você está com Obesidae Grau II (mórbida)')