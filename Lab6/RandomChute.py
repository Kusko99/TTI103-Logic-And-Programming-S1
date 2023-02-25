import random
x = random.randint(1,10)
#chute = int(input("Chute:"))
#while chute != x:
#    print ('tente novamente')
#    chute = int(input())
#print('aeeeeee')
tentativas=int(input("quantas tentativas você quer ter: "))
while(tentativas>10) or (tentativas<1):
    print("a tentaiva tem que ser entre 1 e 10")
    tentativas=int(input("quantas tentativas você quer ter: "))
else:
    for i in range(tentativas):
        chute = int(input("chuta algo: "))
        if(chute == x):
            print("voce acertou")
            break
        else:
            tentativas -=1 
            print(f"voce tem {tentativas} tentativas sobrando")
    print("que pena voce errou")

    
        