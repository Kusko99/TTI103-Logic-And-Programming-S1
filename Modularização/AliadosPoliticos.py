from random import randint, seed
def gera_votos(num_votos):
    return [randint(0,1) for _ in range(num_votos)]
# essa é para um produto escalar mesmo
def concordancia(lista1,lista2):
    return sum([aux[0]*aux[1] for aux in zip(lista1,lista2)])

#teste para função gera_votos
# seed(10)
# votos1 = gera_votos(5)
# print(votos1)
# seed(10)
# votos2 = gera_votos(8)
# print(votos2)
#teste para função concordancia
seed(21)
votos1 = gera_votos(10)
print(votos1)
votos2 = gera_votos(10)
print(votos2)
print(concordancia(votos1,votos2))