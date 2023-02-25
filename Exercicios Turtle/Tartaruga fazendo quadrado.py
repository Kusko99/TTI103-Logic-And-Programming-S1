import turtle

#constantes
LADO = 200
ESPESSURA = 5
VELOCIDADE = 2

#criando uma janela
janela = turtle.Screen()
janela.title('Minha tartaruginha')
janela.bgcolor('black')
janela.screensize(500,500)

#Criando uma tartaruga
Carolina = turtle.Turtle()
Carolina.shape('turtle')
Carolina.pensize(ESPESSURA)
Carolina.speed(VELOCIDADE)
Carolina.color('red')

#Desenhando um quadro colorido
'''Carolina.pencolor('purple')
Carolina.forward(LADO)
Carolina.left(90)
Carolina.pencolor('pink')
Carolina.forward(LADO)
Carolina.left(90)
Carolina.pencolor('red')
Carolina.forward(LADO)
Carolina.left(90)
Carolina.pencolor('orange')
Carolina.forward(LADO)
Carolina.left(90)'''

#desenhando de um jeito inteligente
cores = {'purple','pink','blue','red'}
for cor in cores:
    Carolina.pencolor('cor')
    Carolina.forward(LADO)
    Carolina.left(90)

#fechando a janela
janela.exitonclick()
turtle.TrutleScreen._RUNNING = True

#tentativa 2

#importação de modulos

import turtle
import math

#cria janela
janela = turtle.Screen()
janela.title('quadrado aleatório')
janela.bgcolor('white')
janela.screensize(500,500)

#entrando variaveis
LADO = 100
ESPESSURA = 5
VELOCIDADE = 10
RAIZ = 2
COR_QUADRADO = 'blue'

#calculando raiz
R_RAIZ = math.sqrt(RAIZ)

#criando tartaruga
Gustavo = turtle.Turtle()
Gustavo.shape('turtle')
Gustavo.pensize(ESPESSURA)
Gustavo.speed(VELOCIDADE)
Gustavo.color('blue')

#tartaruga desenhando quadrado
Gustavo.penup()
Gustavo.left(45)
Gustavo.forward(RAIZ*LADO/2)
Gustavo.left(135)
Gustavo.pendown()
for quadrado in range(4):
  Gustavo.forward(LADO)
  Gustavo.left(90)
Gustavo.fillcolor(COR_QUADRADO)
Gustavo.begin_fill()
Gustavo.end_fill()

#fecha janela
janela.exitonclick()
turtle.TrutleScreen._RUNNING = True