testes = int(input())
total = 0
totalCoelhos = 0
totalRatos = 0
totalSapos = 0
for tentativas in range(testes):
    quantidade,tipo=input().split()
    quantidade=int(quantidade)
    total += quantidade
    if tipo == "C":
        totalCoelhos += quantidade
    elif tipo == "R":
        totalRatos += quantidade
    elif tipo == "S":
        totalSapos += quantidade
percentualCoelhos = (totalCoelhos*100)/total
percentualRatos = (totalRatos*100)/total
percentualSapos = (totalSapos*100)/total

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {totalCoelhos}")
print(f"Total de ratos: {totalRatos}")
print(f"Total de sapos: {totalSapos}")
print(f"Percentual de coelhos: {percentualCoelhos:.2f} %")
print(f"Percentual de ratos: {percentualRatos:.2f} %")
print(f"Percentual de sapos: {percentualSapos:.2} %")