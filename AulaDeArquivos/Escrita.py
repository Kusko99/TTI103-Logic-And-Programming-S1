#arquivo a ser lido tem que estar no mesmo diretório onde estou codando
from re import A


arq = open('Exeperimetos.txt','a')
exps = int(input("Quantos novos experimentos? "))
print("Digite os dados dos novos experimentos: ")
for exp in range(exps):
    dado = input()
    arq.write(dado)
arq.close()