n = int(input("Digite o valor de n: "))
j = int(input("Digite o valor de J: "))
m = int(input("Digite o valor de m: "))
congruentes = []
for i in range(n):
    if i%m == j%m:
        congruentes.append(i)
for i in range(len(congruentes)):
    print(congruentes[i])
    
