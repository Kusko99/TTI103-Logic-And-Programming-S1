dic = {'Livia':21,'Enzo':18,'Denis':20,'Daniela':17}
print(dic['Denis'])
print(dic['Livia'])
print(dic['Enzo'])
#Interação nas chaves e valores do dicinário
for (chave,valor) in dic.items():
    print(chave,'=',valor)
dic['Denis']=28
print(dic['Denis'])
print('Livia' in dic)
#Interação nas chaves do dicinário
for nome in dic:
    print(nome)
#Método Values
for valor in dic.values():
    print(valor)
#Método Keys
for nome in dic.keys():
    print(nome)
#Comprimento
print(len(dic))
print(dic.items())
print(dic.keys())
print(dic.values())
#ignorando um parâmetro
for (_,valor) in dic.items():
    print(valor)
for _ in range(10):
    print('Metallica')
saiu = dic.pop('Denis')
print(saiu)
print(dic)
del dic['Enzo']
print(dic)