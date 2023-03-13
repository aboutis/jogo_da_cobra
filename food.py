from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("green")
        self.speed("fastest")
        self.new_loc()

    def new_loc(self):
        random_x = random.randint(-290, 290)
        random_y = random.randint(-290, 290)
        self.goto(x=random_x, y=random_y)

