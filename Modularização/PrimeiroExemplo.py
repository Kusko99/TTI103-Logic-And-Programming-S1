def Cartesiano(listaA,listaB):
    return[(elemA,elemB) for elemA in listaA for elemB in listaB]

def Cart(listA,listB):
    resp = []
    for elemA in listA:
        for elemB in listB:
            resp.append((elemA,elemB))
    return resp

itens = ['camiseta', 'calça', 'bermunda']
marcas = ['Hering', 'Renner', 'Lacoste','Tommy Hillfiger']
produtos = Cartesiano(itens,marcas)
print(produtos)

valores = [num for num in range(2,11)] + list('JQKA')
naipes = ['ouros','espadas','copas','paus']
baralho = Cartesiano(valores,naipes)
print(baralho)

bar = Cart(valores,naipes)
print(bar)