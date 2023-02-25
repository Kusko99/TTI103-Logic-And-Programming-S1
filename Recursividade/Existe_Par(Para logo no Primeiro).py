def existe_par_na_lista(lista_num):
    cont = 0
    for num in lista_num:
        cont += 1
        if num%2 == 0:
            return True, cont
    return False, cont

res1, res2 = existe_par_na_lista([1,2,3,4,5,6])
print(f"iterações: {res2}")
print(f"existe par: {res1}")
