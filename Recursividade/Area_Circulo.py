from math import sqrt, pi

def distancia(x1,y1,x2,y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)

# def area_circulo(raio):
#     return pi*(raio**2)

def area_circulo(x1,y1,x2,y2):
    return pi*(distancia(x1,y1,x2,y2)**2)


# raio = distancia(1,5,4,6)
# area = area_circulo(raio)
# print(area)

# area = area_circulo(distancia(1,5,4,9))
# print(area)

# area = area_circulo(distancia(1,5,4,9))
# print(area)

print(area_circulo(1,5,4,9))