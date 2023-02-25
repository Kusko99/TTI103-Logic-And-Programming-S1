frase = input("Digite um frase: ").lower()
palavras = frase.split(" ")
d = {}
for palavra in palavras:
    if palavra in d:
        d[palavra] += 1
    else:
        d[palavra] = 1

print(d)