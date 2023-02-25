def entrada():
    Dict = {}
    n = int(input("Quantos disparos serão digitados: "))
    for _ in range(n):
        x = int(input("Digite a coordenada x do disparo: "))
        y = int(input("Digite a coordenada y do disparo: "))
        d = (x**2 + y**2)**(1/2)
        pontos = 10 - d//10
        Dict[(x,y)] = pontos
    return Dict

def MaiorPontuacao(Dict):
    PtoMax = max(Dict.values())
    for coordenada in Dict:
        if Dict[coordenada] == PtoMax:
            print(coordenada)

MaiorPontuacao(entrada())