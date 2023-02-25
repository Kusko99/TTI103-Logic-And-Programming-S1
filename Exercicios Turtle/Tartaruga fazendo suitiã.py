#importação
import turtle

#entrada
LADO = 200
VELOCIDADE = 10
ESPESSURA = 5
COR_ESQUERDA = 'red'
COR_DIREITA = 'pink'

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

#desenhando quadrado
Gabriela.left(135)
for lado in range(4):
  Gabriela.forward(LADO)
  Gabriela.left(90)
Gabriela.right(90)
Gabriela.fillcolor(COR_ESQUERDA)
Gabriela.begin_fill()
Gabriela.end_fill()
for lado in range(4):
  Gabriela.forward(LADO)
  Gabriela.right(90)
Gabriela.fillcolor(COR_DIREITA)
Gabriela.begin_fill()
Gabriela.end_fill()

#fecha janela
janela.exitonclick()
turtle.TrutleScreen._RUNNING = True