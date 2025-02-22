from turtle import Turtle
from bullet import Bullet

STARTING_POSITION = (0,-250)
PADDLE_COLOUR = "Green"
PADDLE_SHAPE = "turtle"

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape(PADDLE_SHAPE)
        # self.turtlesize(stretch_len=2, stretch_wid=2)
        self.penup()
        self.left(90)
        self.color(PADDLE_COLOUR)
        self.goto(STARTING_POSITION)
        # Array to hold bullets
        self.bullets = []
        
    def move_right(self):
        self.right(90)
        self.forward(10)
        self.left(90)
        
        
    def move_left(self):
        self.right(90)
        self.backward(10)
        self.left(90)
        
    def shoot(self):
        bullet = Bullet(self.position())
        self.bullets.append(bullet)
        