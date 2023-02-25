def PaRecuriva(n):
    if n == 0: 
        return n
    else: 
        return n + PaRecuriva(n-1)

print(PaRecuriva(10))
print(PaRecuriva(5))
print(PaRecuriva(3 ))