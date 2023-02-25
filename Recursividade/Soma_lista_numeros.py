def soma_recursiva(lista_num,start,end):
    if start > end:
        return 0
    else:
        return lista_num[start] + soma_recursiva(lista_num,start+1,end)

num = list(range(15))
print(soma_recursiva(num,3,8))
