import turtle
import math

#cria janela
janela = turtle.Screen()
janela.title('Símbolo da Mauá')
janela.bgcolor('lightblue')
janela.screensize(500,500)

#entrada de variaveis
LADO = 100
ESPESSURA = 5
VELOCIDADE = 10
NUM_RAIZ = 2 #não mudar
COR_QUADRADO = 'blue'
COR_CIRCULO = 'white'

#criando uma tartaruga
Mariana = turtle.Turtle()
Mariana.shape('turtle')
Mariana.pensize(ESPESSURA)
Mariana.speed(VELOCIDADE)
Mariana.color('blue')

#calcular a raiz quadrada
RAIZ = math.sqrt(NUM_RAIZ)

#indo para o início
Mariana.penup()
Mariana.goto(-LADO/2,-LADO/2)

#Desenhando quadrado de fora
Mariana.pendown()
Mariana.fillcolor(COR_QUADRADO)
Mariana.begin_fill()
for lado in range(4) :
  Mariana.forward(LADO)
  Mariana.left(90)
Mariana.end_fill()

#desenhando o circulo de fora
Mariana.forward(LADO/2)
Mariana.fillcolor(COR_CIRCULO)
Mariana.begin_fill()
Mariana.circle(LADO/2)
Mariana.end_fill()

#desenhando o quadrado de dentro
Mariana.penup()
Mariana.goto(0,0)
Mariana.left(135)
Mariana.forward(LADO/2)
Mariana.left(135)
Mariana.pendown()
Mariana.fillcolor(COR_QUADRADO)
Mariana.begin_fill()
for lado in range(4):
  Mariana.forward(LADO*RAIZ/2)
  Mariana.left(90)
Mariana.end_fill()

#desenhando o circulo de dentro
Mariana.forward(LADO*RAIZ/4)
Mariana.fillcolor(COR_CIRCULO)
Mariana.begin_fill()
Mariana.circle(LADO*RAIZ/4)
Mariana.end_fill()
                    
#fecha janela
janela.exitonclick()
turtle.TrutleScreen._RUNNING = True