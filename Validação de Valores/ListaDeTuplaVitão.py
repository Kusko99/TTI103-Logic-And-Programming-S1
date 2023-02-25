tamanhos = ['P','M','G']
cores = ['branco','preto','vermelho','verde']
camisetas = []
for cor in cores:
    for tamanho in tamanhos:
        camiseta = (cor,tamanho)
        camisetas.append(camiseta)
print(camisetas)