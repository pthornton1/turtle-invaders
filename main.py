from turtle import Screen
from player import Player
from bullet import Bullet
from scoreboard import Scoreboard
from block import Block
from alien import Alien

import time
import random 


# Things to do:
# 2) Detect collisions


ALIEN_COLORS = ("Green")
BLOCK_COLORS = ("Green", "Red", "Yellow")

# HOW MANY TIMES THE ALIENS GO ACROSS THE SCREEN BEFORE GOING DOWN
REPEAT_BEFORE_DESCEND = 1

# HOW MANY TIMES THE ALIENS CAN DESCEND BEFORE THE PLAYER LOSES
MAX_DESCENTS = 20


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
        
# Starting alien direction is right
alien_direction = 'right'
    
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
repeats = 0
descents = 0
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
    
    # MOVE ALIENS
    if alien_direction == 'left':
        
        most_left = 0
        for alien in aliens:
            alien.move_left()
            
        # CHECK IF ALIENS AT LEFT EDGE OF SCREEN
            if alien.position()[0] < most_left:
                most_left = alien.position()[0]
        
        if most_left < -360:
            repeats += 1
            alien_direction = 'right'
        
    else:
        most_right = 0
        for alien in aliens:
            alien.move_right()
            
        # CHECK IF ALIENS AT RIGHT EDGE OF SCREEN
            if alien.position()[0] > most_right:
                most_right = alien.position()[0]
        
        if most_right > 340:
            alien_direction = 'left'
    
    # CHECK IF ALIENS SHOULD DESCEND
    if repeats == REPEAT_BEFORE_DESCEND:
        for alien in aliens:
            alien.descend()
        descents += 1
        repeats = 0

    # CHECK IF BULLET HITS PLAYER
    for bullet in alien_bullets:
        if bullet.player_collision_check(player):
            player.reset()
            scoreboard.lose_life()
            alien_bullets.remove(bullet)

    # CHECK IF BULLET HITS BLOCK
    for bullet in alien_bullets:
        if bullet.block_collision_check(blocks):
            alien_bullets.remove(bullet)
    
    for bullet in player.bullets:
        if bullet.block_collision_check(blocks):
            player.bullets.remove(bullet)
    
    # CHECK IF BULLET HITS ALIEN
    for bullet in player.bullets:
        collision, hit_alien = bullet.alien_collision_check(aliens)
        if collision:
            player.bullets.remove(bullet)
            aliens.remove(hit_alien)
            scoreboard.add_score()
    
    # Check if user out of lives or no more blocks
    if scoreboard.lives == 0 or scoreboard.score == 30 or descents == MAX_DESCENTS:
        for block in blocks:
            block.remove()
        
        for bullet in player.bullets:
            bullet.remove()
        
        for bullet in alien_bullets:
            bullet.remove()
        
        for alien in aliens:
            alien.remove()
        
        scoreboard.game_over()
        game_over = True
    screen.update()

screen.exitonclick()