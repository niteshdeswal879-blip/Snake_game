from turtle import Screen
from snake import Snake
from food import Food
from Scoreboard import Scoreboard
import time
screen=Screen()
screen.setup(height=600, width=600)
screen.title("My snake game")
screen.bgcolor("black")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()


user_input=screen.textinput(title="Choose difficulty", prompt="Easy , Medium , Hard")
if user_input.lower()=="easy":
    d=0.1
elif user_input.lower() == "medium":
    d= 0.07
else:
    d = 0.05
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_on= True
while game_on:
    screen.update()
    time.sleep(d)
    snake.move()

    if snake.segments[0].distance(food)<15:
        food.refresh()
        scoreboard.increase()
        snake.extend()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        scoreboard.reset()
        snake.snake_reset()


    for i in snake.segments[1:]:
        if snake.segments[0].distance(i) < 10:
            scoreboard.reset()
            snake.snake_reset()






screen.exitonclick()