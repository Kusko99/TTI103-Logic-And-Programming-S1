entradaOk = False
while not entradaOk:
    try:
        primeiroTermo = float(input("Digite o primeiro termo: "))
        entradaOk = True
    except:
        print("ERRO, digite um número real!!")
entradaOk = False
while not entradaOk:
    try:
        razao = float(input("Digite a razão: "))
    except:
        print("ERRO, digite um número real!!")
n = 100
an = primeiroTermo+(n-1)*razao
sn = n*(primeiroTermo+an)/2
print(f"A soma dos {n} primeiros termos da PA vale {sn:.3f}")