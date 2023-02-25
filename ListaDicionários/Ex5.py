from re import I


saldo = float(input("Digite o saldo atual da conta: "))
opercao = "x"
conta = {"D":0,"P":0,"S":0}
while opercao != "F":
    print("Escolha a operação:\n(D)epoósito\n(S)aque\n(P)agamento\n(F)im")
    opercao = input("Qual operação: ")
    if opercao == "D":
        conta["D"]+= float(input("Qual o valor do deposito: "))
    elif opercao == "S":
        conta["S"]+= float(input("Qual o valor do saque: "))
    elif opercao == "P":
        conta["P"]+= float(input("Qual o valor do Pagamento: "))

saldo += conta["D"]-conta["P"]-conta["S"]
print(f"O saldo final da sua conta será: {saldo:.2f}")