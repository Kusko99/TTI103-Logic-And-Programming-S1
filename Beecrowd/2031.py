testes = int(input())
jogadas = []
for jogos in range(testes*2):
    jogada = input()
    jogadas.append(jogada)
for partidas in range(0,len(jogadas),2):
    if jogadas[partidas] == "ataque":
        if jogadas[partidas+1] == "ataque":
            print("Aniquilacao mutua")
        else:
            print("Jogador 1 venceu")
    elif jogadas[partidas] == "pedra":
        if jogadas[partidas+1] =="ataque":
            print("Jogador 2 venceu")
        elif jogadas[partidas + 1] == "pedra":
            print("Sem ganhador")
        elif jogadas[partidas + 1] == "papel":
            print("Jogador 1 venceu")
    if jogadas[partidas] == "papel":
        if jogadas[partidas + 1] == "ataque":
            print("Jogador 2 venceu")
        elif jogadas[partidas + 1] == "pedra":
            print("Jogador 2 venceu")
        elif jogadas[partidas + 1] == "papel":
            print("Ambos venceram")