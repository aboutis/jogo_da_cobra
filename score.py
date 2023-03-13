from turtle import Turtle

class Score(Turtle):

    def __init__(self):

        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=260)
        self.hideturtle()
        self.write(f"Placar: {self.score}", move=False, align="center", font=("Arial", 24, "normal"))

    def ganhar_ponto(self):
        self.clear()
        self.score += 1
        self.write(f"Placar: {self.score}", move=False, align="center", font=("Arial", 24, "normal"))

    def fim_jogo(self):
        self.goto(0, 0)
        self.write("FIM DE JOGO",align="center", font=("Arial", 24, "normal"))