from turtle import Screen
from player import Player
from bullet import Bullet
from scoreboard import Scoreboard
from block import Block
from alien import Alien

import time
import random 


# Things to do:
# 1) Get aliens to move
# 2) Detect collisions


ALIEN_COLORS = ("Green")
BLOCK_COLORS = ("Green", "Red", "Yellow")


# SETUP SCREEN
screen = Screen()
screen.setup(height=600,width=800)
screen.title("Turtle Invaders")
screen.bgcolor("Black")
screen.listen()
screen.tracer(0)


# CREATE ON SCREEN ELEMENTS
player = Player()
# ball = Ball()
scoreboard = Scoreboard()


# CREATE ALIEN ARRAY
aliens = []
i = 0
for y in range(200,290,30):
    for x in range(-150,150,30):
        alien = Alien(position=(x,y),color="Red")
        aliens.append(alien)
    
# CREATE BLOCK ARRAY
blocks = []
for y in range(-100,80,60):
    i = 0
    for x in range(-300,300,15):
        if i % 5 == 0:
            x += 60
        block = Block(position=(x,y),color="Green")
        blocks.append(block)
        i+=1

# ALIEN BULLETS
alien_bullets = []

# BIND KEYS
screen.onkey(fun=player.move_left,key="Left")
screen.onkey(fun=player.move_right,key="Right")
screen.onkey(fun=player.shoot,key="space")


#  MAIN LOOP
game_over = False
i = 0
while not game_over:
    time.sleep(0.05)
    
    # MOVE PLAYER BULLETS
    for bullet in player.bullets:
        bullet.move()
    
    # Every 1 second fire a alien bullet from a random alien
    if i == 20:
        i = 0
        random_alien = random.choice(aliens)
        bullet = Bullet(random_alien.position(), player=False)
        alien_bullets.append(bullet)
    i+=1
        
    # MOVE ALIEN BULLETS
    for bullet in alien_bullets:
        bullet.move()
    
    # ball.move()
    
    # Detect Player and Alien Bullet Collisions
    # ball.paddle_collision_check(paddle)
    
    # Detect Block and Alien Bullet Collisions
    # collison, block = ball.block_collision_check(blocks)
    # if collison:
    #     blocks.remove(block)
    #     block.remove()
    #     scoreboard.add_score()
    
    
    # Check if user out of lives or no more blocks
    if scoreboard.lives == 0 or scoreboard.score == 44:
        for block in blocks:
            block.remove()
        scoreboard.game_over()
        game_over = True
    screen.update()

screen.exitonclick()