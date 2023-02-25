import re


def euclides(m,n):
    r = m%n
    while r != 0:
        m = n
        n = r
        r = m % n
        print(m,n,r)
    return n

def euclides_rec(m,n):
    r = m%n
    if r == 0:
        return m
    elif r == 1:
        return 1
    else:
        return euclides_rec(m,r)

print(euclides(20,36))
print(euclides_rec(20,36))