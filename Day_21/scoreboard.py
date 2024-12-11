from turtle import Turtle
FONT = ("Arial", 12, "normal")
SCORE_COLOR = "white"
ALIGNMENT = "center"
POSITION_X = 0
POSITION_Y = 280

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color(SCORE_COLOR)
        self.penup()
        self.setpos(POSITION_X,POSITION_Y)
        self.display_score()

    def display_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        
    def add_score(self):
        self.score += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.home()
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)


class Coordinates(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color(SCORE_COLOR)
        self.penup()
        self.setpos(150,POSITION_Y)


    def display_pos(self, snakeHead):
        self.write(snakeHead.position(), align=ALIGNMENT, font=FONT)
        