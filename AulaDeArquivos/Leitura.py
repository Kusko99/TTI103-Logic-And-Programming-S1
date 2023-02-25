#arquivo a ser lido tem que estar no mesmo diretório onde estou codando
arq = open('Exeperimetos.txt','r')
conteudo = arq.read()
arq.close()
print(conteudo)
