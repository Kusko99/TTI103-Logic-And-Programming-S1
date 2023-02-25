def SomaTudo(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        primeiro = lista[0]
        restante = SomaTudo(lista[1:])
        return primeiro + restante

print(SomaTudo([1,2,3,4,5,6,7,8]))