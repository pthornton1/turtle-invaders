from turtle import Turtle

FONT = ("Courier",12, "normal")
COLOR = "White"
L_POSITION = (-250,270)
R_POSITION = (250,270)
ALIGNMENT = "center"

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.hideturtle()
        self.penup()   
        
        self.score = 0
        self.lives = 4
        self.write_score()
        
    def write_score(self):
        self.clear()
        self.goto(L_POSITION)
        self.write(f"Lives: {self.lives}", align=ALIGNMENT, font=FONT) 
        self.goto(R_POSITION)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT) 
        
    def add_score(self):
        self.score += 1
        self.write_score()
              
    def lose_life(self):
        self.lives -= 1
        self.write_score()
        
    def game_over(self):
        self.goto(0,0)
        if self.lives == 0:
            self.write("Game Over", align=ALIGNMENT, font=FONT)
        else:
            self.write("Game Over", align=ALIGNMENT, font=FONT)