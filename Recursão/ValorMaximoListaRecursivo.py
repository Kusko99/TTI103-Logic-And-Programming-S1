def max_valor(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        primeiro = lista[0]
        max_demais = max_valor(lista[1:])
        if max_demais > primeiro:
            return max_demais
        else:
            return primeiro

def max_valor2(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        max_demais = max_valor2(lista[1:])
        return max_demais if max_demais > lista[0] else lista[0]
        
print(max_valor([1,2,3,4,5,27,6,7,8]))