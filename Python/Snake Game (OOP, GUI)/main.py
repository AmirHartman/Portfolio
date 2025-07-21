from snake import Snake
from time import sleep
from turtle import Screen
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor('black')
screen.title('my snake game'.title())
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


def stop_game():
    global game_is_on
    game_is_on = False


# key bindings
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(stop_game, "Escape")

game_is_on = True

while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()

    # Food system
    if snake.head.distance(food) < 20:
        scoreboard.score += 1
        scoreboard.update_scoreboard()
        food.refresh()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset_snake()
        scoreboard.reset_score()

    # Detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            snake.reset_snake()
            scoreboard.reset_score()

screen.bye()
