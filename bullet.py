from turtle import Turtle
import math

SHAPE = 'square'
SIZE = 1
BULLET_COLOUR = "White"
SCREEN_HEIGHT_LIMIT = 280
SCREEN_PADDLE_LIMIT = -225
SCREEN_WIDTH_LIMIT = 375
BALL_MOVEMENT = 10
STARTING_POSITION = (0,-230)

class Bullet(Turtle):
    
    def __init__(self, position, player=True):
        super().__init__()
        self.shape(SHAPE)
        self.color(BULLET_COLOUR)
        self.penup()
        self.turtlesize(stretch_len=0.5, stretch_wid=0.2)
        self.goto(position)
        
        # If a player bullet go up otherwise go down on screen
        if player == True:
            self.left(90)
        else:
            self.right(90)
        
    def move(self):
        self.forward(BALL_MOVEMENT)
        
        
    def player_collision_check(self, player):
        if self.distance(player) < 15:
            self.remove()
            return True

        return False
        
    def block_collision_check(self, blocks):
        for block in blocks: 
            x_distance = math.sqrt((self.xcor()-block.xcor())**2)
            y_distance = math.sqrt((self.ycor()-block.ycor())**2)
            
            # check which direction the collision is in relation to the block
            if x_distance < 10 and y_distance < 25:
                block.remove()
                self.remove()
                return True
            
        return False  
    
    def alien_collision_check(self, aliens):
        for alien in aliens: 
            if self.distance(alien) < 15:
                self.remove()
                alien.remove()
                return True, alien
        return False, None
    
    def remove(self):
        self.goto(1000,1000)
        self.hideturtle()