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
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.color(SCORE_COLOR)
        self.penup()
        self.setpos(POSITION_X,POSITION_Y)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def add_score(self):
        self.score += 1
        self.display_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.display_score()


class Coordinates(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color(SCORE_COLOR)
        self.penup()
        self.setpos(150,POSITION_Y)


    def display_pos(self, snakeHead):
        self.write(snakeHead.position(), align=ALIGNMENT, font=FONT)
        