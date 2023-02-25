# def maior_que(lista,limite=7):
#     resp = []
#     for elem in lista:
#         if elem > limite:
#             resp.append(elem)
#     return resp

def maior_que(lista,limite=7):
    #lista = [1,2,3]
    return [num for num in lista if num>limite]
    #list compression

teste = [1,2,3,4,5,6,7,8,9,10]
saida = maior_que(teste,5)
print(saida)
outra_saida = maior_que(teste)
print(outra_saida)

lista = [4,5,-6,0,56,48]
limite = 0
resp = maior_que(lista,limite)
print(resp)