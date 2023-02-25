# =============================================================================
# Entrada de dados
# =============================================================================
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
while not (masas_ok and tipo_massa_ok):
    try:
        massa = float(input("Dgite a sua massa em [kg]: "))
        tipo_massa_ok = True
        if massa <= 0:
            print('Erro: a massa deve ser positiva!')
        else:
            massa_ok = True
        except ValueError:
            print('Erro: A massa deve ser número real positivo!')
# =============================================================================
#  Cálculo do IMC           
# =============================================================================
IMC = massa / altura ** 2

# =============================================================================
# Classificação
# =============================================================================
if IMC < 18.5:
    classificacao = 'Abaixo do peso'
elif IMC < 25:
    classificacao = 'Saudável'
elif IMC < 30:
    classificacao = 'Peso em excesso'
elif IMC < 35:
    classificacao = 'Obesidade grau 1'
elif IMC < 40:
    classificacao = 'Obesidade grau 2 (severa)'
elif IMC < :
    calssificacao = 'Obesidade grau 3 (morbida)'
print(f'\nSeu IMC vale {IMC:,.2f')
print("Sua classificação é: ",classificacao)