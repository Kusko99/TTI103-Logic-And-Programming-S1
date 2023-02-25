notas = []
pesos = []
for i in range(3):
    notas.append(int(input()))
for i in range(3):
    pesos.append(int(input()))
media = (notas[0]*pesos[0])+(notas[1]*pesos[1])+(notas[2]*pesos[2])/sum(pesos)
print(f"{notas:.1f}")
