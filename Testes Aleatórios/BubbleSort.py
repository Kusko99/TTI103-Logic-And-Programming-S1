def bubbleSort(lista):
    for _ in range(len(lista)-1):
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista
                
        
print(bubbleSort([6,1,3,4,7,5,2]))