gritos = 0
loteria = []
numero = 0
while gritos < 3:
    piscadas = list(input().split())
    tamanhoDaLista=len(piscadas)
    for lida in range(tamanhoDaLista):
        if piscadas[lida] == "*":
            numero += 1
        elif piscadas[lida] == "-":
            numero += 0
        elif piscadas[0] == "caw":
            gritos += 1
            loteria.append(numero)
            numero = 0
            break
print(*loteria,sep='\n')    
   

