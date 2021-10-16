# Creare la nostra finestra di gioco
# Creare il nostro snake e farlo muovere (giù, su, destra, sinistra)
# creare il cibo per snake e farlo crescere ogni volta che il cibo "viene mangiato"
# fermare il gioco quando lo snake tocca gli estremi della nostra schermata di gioco oppure quando tocca se stesso
# come tenere traccia del punteggio

from turtle import Turtle, Screen
from time import sleep
from random import randint

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
posizioni = [(0,0),(-20,0), (-40,0)]
snake = []
for pos in posizioni:
    s = Turtle("square")
    s.penup()
    s.goto(pos)
    snake.append(s)

food = Turtle("circle")
food.color("red")
x_food = randint(-280, + 280)
y_food = randint(-280, + 280)
food.penup()
food.goto(x_food, y_food)

punti = 0
score = Turtle()
score.penup()
score.hideturtle()
score.goto(x = 0, y = 250)
score.write(f"Score: {punti}", align="center", font=("Oswald", 22, "normal"))


def up():
    if snake[0].heading() != 270:
        snake[0].setheading(90)

def down():
    if snake[0].heading() != 90:
        snake[0].setheading(270)

def left():
    if snake[0].heading() != 0:
        snake[0].setheading(180)

def right():
    if snake[0].heading() != 180:
        snake[0].setheading(0)

def game_over():
    fine = Turtle()
    fine.penup()
    fine.hideturtle()
    fine.write("GAME OVER", align="center", font=("Oswald", 22, "normal"))


screen.listen()
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")



start = True

while start:
    screen.update()
    sleep(0.1)
    for num in range(len(snake) -1,0, -1):
        x = snake[num-1].xcor()
        y = snake[num-1].ycor()
        snake[num].goto(x,y)
    snake[0].forward(20)

    if snake[0].distance(food) < 15:
        food.goto(randint(-280, 280), randint(-280, 280))
        quadrato = Turtle("square")
        quadrato.penup()
        quadrato.goto(x = snake[-1].xcor(), y = snake[-1].ycor())
        snake.append(quadrato)
        punti+= 1
        score.clear()
        score.write(f"Score: {punti}", align="center", font=("Oswald", 22, "normal"))


    # collisioni con il muro
    if snake[0].xcor() > 280 or snake[0].xcor() < -280 or snake[0].ycor() > 280 or snake[0].ycor() < -280:
        start = False
        game_over()



    # collisioni con se stesso
    for q in snake[1:]:
        if q.distance(snake[0]) < 10:
            start = False
            game_over()



screen.exitonclick()
