import turtle

# Criando canvas
wn = turtle.Screen()       
wn.bgcolor('lightblue')
tartaruga = turtle.Turtle()

# Apontando pra baixo e removendo a caneta
tartaruga.right(90)
tartaruga.penup()

# Escrevendo!
fonte1 = ("Comic Sans", 20, "italic")
tartaruga.write("Lógica ", False, "center", fonte1)
tartaruga.forward(40)
fonte2 = ("Comic Sans", 20, "normal")
tartaruga.write("de", False, "center", fonte2)
tartaruga.forward(40)
fonte3 = ("Comic Sans", 30, "bold")
tartaruga.write("Programação", False, "center", fonte3)

wn.exitonclick()
turtle.TurtleScreen._RUNNING = True