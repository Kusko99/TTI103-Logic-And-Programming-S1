frase = input("Digite um frase: ").replace(" ","").lower()

d = {}
for char in frase:
    if char in d:
        d[char] += 1
    else:
        d[char] = 1

print(d)
