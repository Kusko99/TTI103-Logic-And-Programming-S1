from random import choice
def criar_baralho():
    NUM_CARTAS = 13
    MIN_VALOR = 2
    MAX_VALOR = 10
    aux_nomes = [str(i) for i in range(MIN_VALOR,MAX_VALOR+1)]
    nomes = ['Ás'] + aux_nomes + ['Valete','Damas','Rei']
    aux_chaves = [nome + ' de ' for nome in nomes]
    naipes = ['Ouros','Espadas','Copas','Paus']
    chaves = [aux_chave + naipe for naipe in naipes for aux_chave in aux_chaves]
    valores = list(range(1,MAX_VALOR)) + [MAX_VALOR]*4
    baralho = {chave:valor for i in range(len(naipes)-1) for(chave,valor) in zip(chaves[i*NUM_CARTAS:NUM_CARTAS*(i+1)],valores)}
    return baralho

def distribuir(baralho,desce,cartas,pontuacao):
    cartas_mao = []
    pontuacao = 0
    for i in range(desce):
        carta = (choice(baralho))
        cartas_mao.append(carta)
        pontuacao += baralho[carta]
        print(cartas_mao)
        print(pontuacao)
        del baralho[carta]
    return cartas_mao,pontuacao

def distribuir_cartas(baralho):
    cartas_jogador,pontuacao_jogador,cartas_mesa,pontuacao_mesa = [],[],[],[]
    cartas_jogador,pontuacao_jogador = distribuir(baralho,2,cartas_jogador,pontuacao_jogador,)
    cartas_mesa,pontuacao_mesa = distribuir(baralho,2,cartas_mesa,pontuacao_mesa)
    cartas_jogadas = 4
    while cartas_jogadas < len(baralho):
        desce = input("Quer mais cartas? (s/n): ")
        if desce == 's':
            cartas_jogador,pontuacao_jogador = distribuir(baralho,1,cartas_jogador,pontuacao_jogador,)
            cartas_mesa,pontuacao_mesa = distribuir(baralho,1,cartas_mesa,pontuacao_mesa)
            cartas_jogadas += 2
        elif desce == 'n':
            break
        elif pontuacao_jogador >= 21 or pontuacao_mesa >= 21:
            print("Acabou!!!")
            break
    if pontuacao_jogador == 21 or pontuacao_mesa > 21 or (pontuacao_jogador > pontuacao_mesa and pontuacao_jogador < 21):
        print("JOGADOR GANHOU!!!")
    elif pontuacao_mesa == 21 or pontuacao_jogador > 21 or (pontuacao_jogador < pontuacao_mesa and pontuacao_mesa < 21):
        print("MESA GANHOU!!! CASA FELIZ =)")
    else:
        print("Empate")

distribuir_cartas(criar_baralho())