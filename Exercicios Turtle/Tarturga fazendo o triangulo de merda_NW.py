#importação
import turtle
import math

#entrada
ALTURA = 100
VELOCIDADE = 10
ESPESSURA = 5

#cria janela
janela = turtle.Screen()
janela.title('Sutiã')
janela.bgcolor('lightblue')
janela.screensize(500,500)

#criando uma tartaruga
Gabriela = turtle.Turtle()
Gabriela.shape('turtle')
Gabriela.pensize(ESPESSURA)
Gabriela.speed(VELOCIDADE)
Gabriela.color('blue')

#seno e tangente de 45
seno_45 = math.sin(45)
tan_45 = math.tan(45)

#fazendo triangulo maior
Gabriela.left(90)
Gabriela.forward(ALTURA/tan_45)
Gabriela.right(135)
Gabriela.forward(ALTURA/seno_45)
Gabriela.right(135)
Gabriela.forward(ALTURA/seno_45)
Gabriela.forward(ALTURA/tan_45)

#fazendo triangulo menor

#fecha janela
janela.exitonclick()
turtle.TrutleScreen._RUNNING = True