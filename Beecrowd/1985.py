tamanhoCompra=int(input())
totalCompra=0
for compra in range(tamanhoCompra):
    produto,quantidade=input().split()
    quantidade=int(quantidade)
    if produto == "1001":
        totalCompra += 1.5*quantidade
    elif produto == "1002":
        totalCompra += 2.5*quantidade
    elif produto == "1003":
        totalCompra += 3.5*quantidade
    elif produto == "1004":
        totalCompra += 4.5*quantidade
    elif produto == "1005":
        totalCompra += 5.5*quantidade
print(f"{totalCompra:.2f}")
