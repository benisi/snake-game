from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from score_board import ScoreBoard

BOUNDARY = 300

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

food = Food()
snake = Snake()
score_board = ScoreBoard()

def start_game():
    game_on = True
    while game_on:
        sleep(0.1)
        screen.update()
        snake.move()
        
        if snake.head.distance(food) < 15:
            food.refresh_position()
            score_board.increase()
            snake.grow()
        
        y_cor = snake.head.ycor()
        x_cor = snake.head.xcor()
        
        if y_cor > BOUNDARY or y_cor < -BOUNDARY or x_cor > BOUNDARY or x_cor < -BOUNDARY:
            game_on = False
            score_board.game_over()
            
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 5:
                game_on = False
                score_board.game_over()

def restart():
    score_board.reset()
    snake.refresh()
    start_game()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')  
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
screen.onkey(restart, 'Return')
        
start_game()
screen.exitonclick()