def entrada():
  frase = str(input())
  vogal = 0 
  return vogal, frase
def contagem(vogal, frase):
  for letra in frase:
    if letra in "aeiou":
      vogal+=1
  return vogal
def metodos():
  vogal, frase = entrada()
  vogal = contagem(vogal, frase)
  print(vogal)

metodos()