def entrada():
    return input("Digite sua frase: ")

def pig_latin(frase):
    palavras = frase.split()
    fraseFinal = []
    for i in range(len(palavras)):
        palavra = palavras[i]
        palavra = palavra[1:] + palavra[0] + 'ay'
        fraseFinal.append(palavra)
    return ' '.join(fraseFinal)

print(pig_latin(entrada()))