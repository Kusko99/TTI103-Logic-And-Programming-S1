#Recebe as variaveis

BASE = float(input("Digite a base do triangulo: "))
ALTURA = float(input("Digite a altura do triangulo: "))

#Calcula a area do triangulo

AREA = (BASE*ALTURA)/2

#Mostra a area

#print('A área do triângulo é: ', AREA )

print(f'A área do triângulo de base {BASE:,.2f} e altura {ALTURA:,.2f} é {AREA:,.2f}')