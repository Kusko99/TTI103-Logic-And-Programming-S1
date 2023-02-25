valores = []
valor = 0
while not valor < 0:
    valor = int(input("Digite um valor: "))
    if valor >= 0:
        valores.append(valor)
if valores == []:
    print("Lista vazia")
else:
    media = sum(valores)/len(valores)
    print(f"A média dos valores digitados é {media}")