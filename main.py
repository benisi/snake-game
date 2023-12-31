from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from score_board import ScoreBoard

BOUNDARY = 300
DELAY_DIVISOR = 10
DELAY_MULTIPLIER = 0.02
MAX_DELAY = 0.1


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

food = Food()
snake = Snake()
score_board = ScoreBoard()

def start_game():
    while score_board.game_on:
        sleep(MAX_DELAY - (int(score_board.score / DELAY_DIVISOR)) * DELAY_MULTIPLIER)
        screen.update()
        snake.move()
        
        if snake.head.distance(food) < 15:
            food.refresh_position()
            score_board.increase()
            snake.grow()
        
        y_cor = snake.head.ycor()
        x_cor = snake.head.xcor()
        
        if y_cor > BOUNDARY or y_cor < -BOUNDARY or x_cor > BOUNDARY or x_cor < -BOUNDARY:
            score_board.game_over()
            
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 5:
                score_board.game_over()

def restart():
    if not score_board.game_on:
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