from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import Score
is_game_on = True
screen = Screen()
screen.tracer(0)
screen.setup(width=600 , height=600)
screen.bgcolor("black")
screen.title("Saap Ka Khel")
segment_position = [(0, 0), (-20, 0), (-40, 0)]
segment = []
saap = Snake()

khanna = Food()
score_board = Score()
screen.listen()
screen.onkey(saap.up, "Up")
screen.onkey(saap.down, "Down")
screen.onkey(saap.left, "Left")
screen.onkey(saap.right, "Right")

while is_game_on:
    screen.update()
    time.sleep(0.1)

    saap.move()
    if saap.head.distance(khanna) < 15 :
        khanna.refresh()
        saap.extend()
        score_board.increase_score()

    if saap.head.xcor() > 280 or saap.head.xcor() < -280 or saap.head.ycor() > 280 or saap.head.ycor() < -280:
        is_game_on = False
        score_board.game_over()


    for segment in saap.segment :
        if segment == saap.head:
            pass
        elif saap.head.distance(segment) < 10:
            is_game_on = False
            score_board.game_over()




screen.exitonclick()