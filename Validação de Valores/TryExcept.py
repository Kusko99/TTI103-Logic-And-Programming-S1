'''#alternativa1
a1= input("Digite o primero termo: ")
while type(a1) != float:
    try:
        a1 = float(a1)
    except:
        print('ERRO: Digite um valor real!')
        a1 = input("Primeiro termo de PA: ")
print(a1)
print(type(a1))'''
'''#alternativa2
a1= input("Digite o primero termo: ")
while True:
    try:
        a1 = float(a1)
        break
    except:
        print('ERRO: Digite um valor real!')
        a1 = input("Primeiro termo de PA: ")'''
#alternativa3
entrada_ok = False
while not entrada_ok:
    try:
        a1 = float(input("Primeiro termo: "))
        entrada_ok = True
    except:
        print('ERRO: Digite um valor real!')