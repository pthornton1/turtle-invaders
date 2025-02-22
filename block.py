from turtle import Turtle

BLOCK_LENGRH = 0.5
BLOCK_WIDTH = 2
BLOCK_SHAPE = "square"

class Block(Turtle):
    
    def __init__(self, position=(0,0), color="White"):
        super().__init__()
        self.shape(BLOCK_SHAPE)
        self.turtlesize(stretch_len=BLOCK_LENGRH, stretch_wid=BLOCK_WIDTH)
        self.penup()
        self.color(color)
        # self.left(90)
        self.goto(position)
    
    def remove(self):
        self.goto(1000,1000)
        self.hideturtle()