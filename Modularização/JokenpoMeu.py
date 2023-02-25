import random
def entrada ():
    entrada_ok = False
    txt = "JO KEN PO"
    while not entrada_ok:
        try:
            print(txt.center(40,'*'))
            print("\nMenu de Opções")
            print("[0] Pedra")
            print("[1] Papel")
            print("[2] Tesoura")
            jogada = int(input("Escolha uma opção: "))
            if (jogada == 0 or jogada == 1 or jogada == 2):
                entrada_ok = True
        except:
            print("\nEscolha uma opção")
    return jogada
def computador():
    jogada = random.randint(0,2)
    if jogada == 0:
        jogou = "Pedra"
    elif jogada == 1:
        jogou = "Papel"
    elif jogada == 2:
        jogou = "Tesoura"
    return jogada,jogou
def jogo(jogador1, computador):
    if (jogador1 == 0):
        if (computador == 0):
            resultado = "Empate"
        elif(computador == 1):
            resultado = "Perdeu!!"
        elif(computador == 2):
            resultado = "Ganhou!!"
    elif (jogador1 == 1):
        if (computador == 0):
            resultado = "Ganhou!!"
        elif(computador == 1):  
            resultado = "Empate"
        elif(computador == 2):
            resultado = "Perdeu!!"
    elif (jogador1 == 2):
        if (computador == 0):
            resultado = "Perdeu!!"
        elif(computador == 1):
            resultado = "Ganhou!"
        elif(computador == 2):
            resultado = "Empate"
    return resultado
    
#Jogando
jogada_player = entrada()
jogada_pc,jogou_pc = computador()
resultado = jogo(jogada_player,jogada_pc)
print(f"\nO computaodor jogou {jogou_pc}\n")
print(resultado)
