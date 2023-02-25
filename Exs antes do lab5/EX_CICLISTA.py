import turtle

#cria janela
janela = turtle.Screen()
janela.title('Símbolo da Mauá')
janela.bgcolor('lightblue')
janela.screensize(1000,1000)

#entrando variaveis

VELOCIDADE = 10

#criando ciclista
ciclista = turtle.Turtle()
ciclista.shape('turtle')
ciclista.speed(VELOCIDADE)

#fazendo caminho do ciclista
ciclista.left(90)
ciclista.forward(100)
ciclista.right(38)
ciclista.forward(200)
ciclista.left(57)
ciclista.forward(50)
ciclista.right(9)
ciclista.right(10)

#fecha janela
janela.exitonclick()
turtle.TrutleScreen._RUNNING = True