#leitura do arquivos alunos
arq_alunos = open("alunos.txt",'r')
alunos = arq_alunos.read().split()
arq_alunos.close() 
#leitura das notas dos alunos
arq_notas = open("notas.txt",'r')
medias = []
for linha in arq_alunos:
    notas = list(map(float,linha.split()))
    medias.append(sum(notas)/len(notas))
arq_notas.close()
#criação do arquivo de médias dos alunos
arq_alunos_media = open('Medias.txt','w')
arq_alunos_media.write('***Médias Finais e Estatística***\n')
arq_alunos_media.write('***Alunos e Médias **\n')
apv, rep = 0,0
for indice in range(len(alunos)):
    final = medias[indice]
    if final >= 6.0:
        situacao = 'Aprovado'
    else:
        situacao = 'Reprovado'
        rep += 1
    linha = alunos[indice] + ' ' + f'{final:.1f}'