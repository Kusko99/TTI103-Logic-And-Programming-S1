def existe_par_na_lista(lista_num):
    cont = 0
    for num in lista_num:
        cont += 1
        if num%2 == 0:
            return True, cont
    return False, cont

def pares_na_lista(lista_num):
    pares = []
    for num in lista_num:
        if num%2 == 0:
            pares.append(num)
    return pares

def pares_na_lista_pythonico(lista_num):
    return [num for num in lista_num if num%2 == 0]

res1, res2 = existe_par_na_lista([1,2,3,4,5,6])
print(f"iterações: {res2}")
print(f"existe par: {res1}")
list_pares = pares_na_lista([1,2,3,4,5,6])
print(list_pares)
list_pares = pares_na_lista([1,3,5,7])
print(list_pares)
list_pares = pares_na_lista_pythonico([1,2,3,4,5,6])
print(list_pares)
list_pares = pares_na_lista_pythonico([1,3,5,7])
print(list_pares)