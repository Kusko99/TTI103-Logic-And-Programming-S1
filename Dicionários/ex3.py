texto = '''So you are looking for a cool font? Different people have different purposes when looking for a cool font so they may have different opinions on what a cool font is. For example, a cool font for graffiti and a cool font for logo design may be very different things. To make things easier for you and help you find the cool fonts for your project, we would like to suggest you browse our font collections first, generate a preview of them. Depending on different projects, you might take a look at our popular pages like tattoo fonts, graffiti fonts, cursive fonts, etc.'''.lower()
pontuacao = [",",",","!","?","*","'",'"']
for p in pontuacao:
    texto = texto.replace(p," ")
palavras = texto.split()
#split devolve lista com palavras como itens
numero_palavras = len(palavras)
print(palavras)
print(numero_palavras)
#Criação do dicionário para contagem de palavras
dict_palavras = {}
for palavra in palavras:
   freq = palavras.count(palavra) 
   dict_palavras[palavra] = freq
   while freq != 0:
       del palavras[palavras.index(palavra)]
       freq -= 1
print(dict_palavras)