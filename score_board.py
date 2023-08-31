from turtle import Turtle

ALIGN='center'
FONT=('Courier', 16, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.setup()
    
    def setup(self):
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.update()
        self.hideturtle()
        self.game_on = True
        
    def update(self):
         self.clear()
         self.write(f'Score {self.score}', move=False, align=ALIGN, font=FONT) 
         
    def game_over(self):
        self.game_on = False
        self.goto(0, 0)
        self.write('Game Over', move=False, align=ALIGN, font=FONT) 
        self.goto(0, -20)
        self.write('Press ENTER to play again', move=False, align=ALIGN, font=FONT)
    
    def reset(self):
        self.setup()
        self.update()
        
    def increase(self):
        self.score += 1
        self.update()
 