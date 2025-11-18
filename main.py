from turtle import Screen,Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

difficulty = screen.textinput("Difficulty", "Choose: easy / medium / hard")
speed = {"easy":0.15, "medium":0.1, "hard":0.05}.get(difficulty, 0.1)


game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(speed)

    snake.move()

    # detect collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    #detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()< -280 or snake.head.ycor()>280 or snake.head.ycor() < -280:
        game_is_on =False
        scoreboard.game_over()

    #detect collision with tail
    for s in snake.segments[1:]:
        if snake.head.distance(s)<10:
            game_is_on=False
            scoreboard.game_over()


screen.exitonclick()
