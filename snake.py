from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 10
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:
    def __init__(self):
        self.create_snake()
    
    def move(self):
        for part_num in range(len(self.segments) - 1, 0, -1):
            new_x_pos = self.segments[part_num - 1].xcor()
            new_y_pos = self.segments[part_num - 1].ycor()
            self.segments[part_num].goto(new_x_pos, new_y_pos)
        self.segments[0].forward(MOVE_DISTANCE)

    def create_snake(self):
        self.segments = []
        for pos in STARTING_POSITIONS:
            self.create_segment(pos)
        self.head = self.segments[0]
    
    def create_segment(self, pos):
        part = Turtle('square')
        part.color("white")
        part.penup()
        part.goto(pos)
        self.segments.append(part)
        
    def refresh(self):
        for segment in self.segments:
            segment.reset()
        self.create_snake()
        
    def grow(self):
        self.create_segment(self.segments[-1].position())
            
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
         if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        
    def left(self):
         if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)