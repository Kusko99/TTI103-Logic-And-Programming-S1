tamanhos = ['P','M','G']
cores = ['branco','preto','vermelho','verde']
tamanhosXcores = []
for i in range(len(tamanhos)):
    x = tamanhos[i]
    for i in range(len(cores)):
        tamanhosXcores.append(f'{x},{cores[i]}')
print(tamanhosXcores)
