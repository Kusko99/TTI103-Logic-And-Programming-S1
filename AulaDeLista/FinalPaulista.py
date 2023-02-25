l1=['Meu','perdeu','do paulistão']
l2=['time','a final','2022']
l3 = []
frase = ''
for indice in range(len(l1)):
    l3.append(l1[indice] + ' ' + l2[indice])
    if (indice != len(l2)-1):
        frase += l3[indice] + ' '
    else:
        frase += l3[indice] + '.'
print(l3)
print(frase)