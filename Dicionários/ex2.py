texto = 'Eduardo me deu uma dic muito boa.'
pontuacao = [",",",","!","?","*","'",'"']
for p in pontuacao:
    texto = texto.replace(p," ")
palavras = texto.split()
#split devolve lista com palavras como itens
numero_palavras = len(palavras)
print(palavras)
print(numero_palavras)