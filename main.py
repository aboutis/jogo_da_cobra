import time
from turtle import Screen
from snakes import Snakes
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Jogo Da Cobrinha")
screen.tracer(0)

snakes = Snakes()
comida = Food()
placar = Score()

continuar_jogo = True
while continuar_jogo:
    screen.update()
    time.sleep(0.1)
    snakes.movimento()
    snakes.control()

    if snakes.lista[0].distance(comida) < 15:
        comida.new_loc()
        snakes.aumentar()
        placar.ganhar_ponto()


    if snakes.lista[0].xcor() > 280 or snakes.lista[0].xcor() < -280 or snakes.lista[0].ycor() > 280 or\
            snakes.lista[0].ycor() < -280:
        continuar_jogo = False
        placar.fim_jogo()

    for seg in snakes.lista:
        if seg == snakes.lista[0]:
            pass
        elif snakes.lista[0].distance(seg) < 10:
            placar.fim_jogo()
            continuar_jogo = False

screen.exitonclick()
