sapos, ratos, coelhos = [], [], []
arq = open('Experiementos.txt','r')
conteudo = arq.read()
exps = conteudo.split('\n')
for exp in exps:
    teste=exp.split()
    if teste[1] == 'S':
        sapos.append(int(teste[0]))
    elif teste[1] == 'R':
        ratos.append(int(teste[0]))
    elif teste[1] == 'C':
        coelhos.append(int(teste[0]))
resultados=open('resultados.txt','w')
resultados.write(f'Total de sapos: {sum(sapos)}'+'\n')
resultados.write(f'Total de ratos: {sum(ratos)}'+'\n')
resultados.write(f'Total de coelhos: {sum(coelhos)}'+'\n')
resultados.close()