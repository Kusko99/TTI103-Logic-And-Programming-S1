N = int(input())
tempo = []
for i in range(N):
    tempo_passado = int(input())
    tempo.append(tempo_passado)
for i in range(len(tempo)):
    ano = 2015 - tempo[i]
    if ano > 0:
        print(f'{ano} D.C.')
    elif ano < 0:
        ano = ano*-1
        print(f'{ano} A.C.')
    elif ano == 0:
        print(f'1 A.C.')