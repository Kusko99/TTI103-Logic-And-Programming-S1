def fatorial_inter(valor):
    if valor >= 0:
        fat = 1
        for num in range(1,valor+1):
            print(num)
            fat *= num
        return fat
    else:
        return None

print(fatorial_inter(5))
print(fatorial_inter(7))
print(fatorial_inter(8000))
print(fatorial_inter(-3))