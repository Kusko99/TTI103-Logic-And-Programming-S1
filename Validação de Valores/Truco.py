naipes = ('Paus', 'Copas', 'Ouros', 'Espadas')
numeros = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')
import collections
carta = collections.namedtuple('carta',['naipe','numero'])
baralho = [carta(naipe,numero)for naipe in naipes for numero in numeros]
