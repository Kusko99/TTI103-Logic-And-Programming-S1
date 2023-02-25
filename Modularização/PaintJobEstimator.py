from math import ceil
def entrada():
    area = float(input("Digite a area em pés quadrados: "))
    precoGalao = float(input("Digite o preço do galão: "))
    return area, precoGalao
def quantidadeGalao(area):
    # a = area//112
    # b = area/112
    # quantidadeGalao = a
    # if a < b:
    #     quantidadeGalao += 1
    #return quantidadeGalao
    return ceil(area/112)
def horaDeTrabalho(area):
    return quantidadeGalao(area)*8
def custoPintura(area, precoGalao):
    return precoGalao*quantidadeGalao(area)
def custoTrabalho(area):
    return horaDeTrabalho(area)*35
def custoTotal(area,precoGalao):
    return custoPintura(area,precoGalao) + custoTrabalho(area)
def principal():
    #entrada de dados
    area,precoGalao = entrada()
    #Processamento
    galoes_tinta = quantidadeGalao(area)
    horas = horaDeTrabalho(area)
    total_tinta = custoPintura(area, precoGalao)
    total_servico = custoTrabalho(area)
    custo = custoTotal(area, precoGalao)
    #saída
    print(f"Serõ necessários {galoes_tinta} galões de tinta")
    print(f"Tempo estimado da obra: {horas} horas")
    print(f"Custo da tinta: ${total_tinta:.2f}.")
    print(f"Custo da mão de obra: ${total_servico:.2f}")
    print(f"Preço total: ${custo:.2f}.")

    if __name__ == '__main__':
        principal()
print(principal())

