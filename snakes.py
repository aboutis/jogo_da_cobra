from turtle import Turtle, Screen


UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

POS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCIA_MOV = 10


class Snakes:

    def __init__(self):
        self.lista = []
        self.movimento()
        self.screen = Screen()
        self.cobra()

    def cobra(self):
        for position in POS:
            self.criar_cobra(position)

    def criar_cobra(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.setposition(position)
        self.lista.append(snake)

    def aumentar(self):
        self.criar_cobra(self.lista[-1].position())

    def movimento(self):
        for bd_snk in range(len(self.lista) - 1, 0, -1):
            novo_x = self.lista[bd_snk - 1].xcor()
            novo_y = self.lista[bd_snk - 1].ycor()
            self.lista[bd_snk].goto(x=novo_x, y=novo_y)
            self.lista[0].forward(DISTANCIA_MOV)


    def control(self):
        def left():
            if self.lista[0].heading() != RIGHT:
                self.lista[0].setheading(LEFT)

        def up():
            if self.lista[0].heading() != DOWN:
                self.lista[0].setheading(UP)

        def down():
            if self.lista[0].heading() != UP:
                self.lista[0].setheading(DOWN)

        def right():
            if self.lista[0].heading() != LEFT:
                self.lista[0].setheading(RIGHT)

        self.screen.onkeypress(up, "Up")
        self.screen.onkeypress(left, "Left")
        self.screen.onkeypress(down, "Down")
        self.screen.onkeypress(right, "Right")
        self.screen.listen()
