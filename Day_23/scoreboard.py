from turtle import Turtle

FONT = ("Courier", 24, "normal")
SCOREBOARD_POSITION = (-290, 260)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.setposition(SCOREBOARD_POSITION)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def add_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=FONT)