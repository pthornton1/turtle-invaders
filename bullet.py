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
        # current_x = self.xcor()
        # current_y = self.ycor()
        
        # # Wall Collision
        # if current_y > SCREEN_HEIGHT_LIMIT:
        #     self.y_direction *= -1
            
        # if current_x**2 > SCREEN_WIDTH_LIMIT**2:
        #     self.x_direction *= -1
            
        # new_y = current_y + BALL_MOVEMENT* self.y_direction
        # new_x = current_x + BALL_MOVEMENT* self.x_direction
        
        # self.goto(x=new_x,y=new_y)
        
        
    def player_collision_check(self, player):
        if self.ycor() < SCREEN_PADDLE_LIMIT and self.distance(player) < 50:
            # avoid double bouncing on the same paddle
            self.y_direction = 1
            self.increase_speed()
        
    def block_collision_check(self, blocks, speed_increase=1):
        for block in blocks: 
            x_distance = math.sqrt((self.xcor()-block.xcor())**2)
            y_distance = math.sqrt((self.ycor()-block.ycor())**2)
            
            # check which direction the collision is in relation to the block
            if 45 < x_distance < 60 and  y_distance < 25:
                self.move_speed *= speed_increase
                self.x_direction *= -1
                return True, block
            if x_distance < 45 and 25 < y_distance < 35:
                self.move_speed *= speed_increase
                self.y_direction *= -1
                return True, block                
                
        return False, None
    
    def increase_speed(self, speed_increase=0.9):
        self.move_speed *= speed_increase
    
    def ball_out_of_bounds(self):
        return self.ycor()< -SCREEN_HEIGHT_LIMIT
        
    
    def who_scored(self):
        if self.xcor() > 1:
            return "left"
        else:
            return "right"