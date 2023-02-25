quad = []
i = 0
for num in range(1,101):
    if num % 2 == 0:
        quad.append(num**2)
        print(f'{num}\t{quad[i]}')
        i += 1
#em uma única linha
#novo_quad = [num**2 for num in range(0,101) if num % 2 == 0]