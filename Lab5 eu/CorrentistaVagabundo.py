#Renda Mínima
Renda_ok = False
Tipo_Renda_ok = False
while not (Renda_ok and Tipo_Renda_ok):
    try:
        Renda = float(input('Digite a sua renda anual: '))
        Renda_ok = True
        if Renda <= 0:
            print('Erro: a renda deve ser positiva!')
        else:
            Tipo_Renda_ok = True
    except ValueError:
            print('Erro: A renda deve ser número real positivo!')
#Emprego fixo
Emprego_ok = False
Tipo_Emprego_ok = False
while not (Emprego_ok and Tipo_Emprego_ok):
    try:
        Emprego = int(input('Digite o tempo que está trabalhando em um emprego fixo em anos: '))
        Emprego_ok = True
        if Emprego <= 0:
            print('Erro: o número de anos deve ser positivo')
        else:
            Tipo_Emprego_ok = True
    except ValueError:
        print('Erro: o número de anos deve ser um número inteiro positivo!')
#estrutura de decisão
if Renda >= 30000 and Emprego >= 2:
    print('''PARABÉNS
    Empresitmo aprovado''')
else:
    print('Emprestimo reprovado')