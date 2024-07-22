from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
score_board = Scoreboard()

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, key="Up")
screen.onkey(snake.left, key="Left")
screen.onkey(snake.down, key="Down")
screen.onkey(snake.right, key="Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        snake.extend()

    #Detect collision with wall
    if snake.head.ycor() < -299 or snake.head.ycor() >= 300 or snake.head.xcor() > 299 or snake.head.xcor() < -299:
        game_is_on = False
        score_board.game_over()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()


screen.exitonclick()
