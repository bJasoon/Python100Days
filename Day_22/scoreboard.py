from turtle import Turtle
SCOREBOARD_COLOR = "white"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color(SCOREBOARD_COLOR)
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.setposition(-100, 200)
        self.write(self.p1_score, align="center", font=("Courier", 80, "normal"))
        self.setposition(100, 200)
        self.write(self.p2_score, align="center", font=("Courier", 80, "normal"))

    def add_score(self, ball_x_cor):
        if ball_x_cor >= 400:
            self.p1_score += 1
            print("Player 1 scored")
        elif ball_x_cor <= -400:
            self.p2_score += 1
            print("Player 2 scored")
        self.update_scoreboard()
