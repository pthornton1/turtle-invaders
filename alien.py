from turtle import Turtle

ALIEN_LENGRH = 1
ALIEN_WIDTH = 1
ALIEN_SHAPE = "turtle"

class Alien(Turtle):
    
    def __init__(self, position=(0,0), color="White"):
        super().__init__()
        self.shape(ALIEN_SHAPE)
        self.turtlesize(stretch_len=ALIEN_LENGRH, stretch_wid=ALIEN_WIDTH)
        self.penup()
        self.color(color)
        self.right(90)
        self.goto(position)
    
    def remove(self):
        self.goto(1000,1000)
        self.hideturtle()
        
    def move_right(self):
        self.right(90)
        self.forward(10)
        self.left(90)
        
        
    def move_left(self):
        self.right(90)
        self.backward(10)
        self.left(90)