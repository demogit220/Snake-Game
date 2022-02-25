from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from turtle import Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # it just tell the program to turn off the automatic updates.
# if turn this off, we have to call update explicitly when we want to update the screen
snake = Snake()
food = Food()  # food is also turtle object
scores = ScoreBoard(screen)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# moving the snake
game_is_on = True

while game_is_on:
    screen.update()  # updating the screen when whole snake has moved forward
    time.sleep(0.1)  # stops the time for given amount of time
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:  # As size of food is 10 *10
        scores.update()
        snake.extend()
        food.refresh()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scores.Reset()
        snake.reset()

    # Detect collision with tail
    # If head collides with any segment, trigger game over.
    for segment in snake.segments[1:]:  # Python slicing
        if snake.head.distance(segment) < 10:
           scores.Reset()
           snake.reset()

screen.exitonclick()
