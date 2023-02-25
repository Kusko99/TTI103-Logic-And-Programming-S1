import math
import cmath

def delta(a,b,c):
    return math.pow(b,2) - 4*a*c

def baskara(a,b,c):
    discriminante = delta(a,b,c)
    if discriminante >= 0:
        x1 = (-b + math.sqrt(discriminante))/(2*a)
        x2 = (-b - math.sqrt(discriminante))/(2*a)
    else:
        x1 = (-b + cmath.sqrt(discriminante))/(2*a)
        x2 = (-b - cmath.sqrt(discriminante))/(2*a)
    return x1, x2

#caso1
x1,x2 = baskara(1,-4,4)
print(x1,x2)
#caso2
x1,x2 = baskara(1,-4,3)
print(x1,x2)
#caso3
x1,x2 = baskara(1,-6,10)
print(x1,x2)
