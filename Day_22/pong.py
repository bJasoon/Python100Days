from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

PLAYER1_X_POS = -350
PLAYER2_X_POS = 350
PLAYER1_UP_KEY = "w"
PLAYER1_DOWN_KEY = "s"
PLAYER2_UP_KEY = "Up"
PLAYER2_DOWN_KEY = "Down"
SCREEN_TIME_REFRESH = 0.1

game_on = True
screen = Screen()

screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

p1_paddle = Paddle(player_x_pos=PLAYER1_X_POS)
p2_paddle = Paddle(player_x_pos=PLAYER2_X_POS)
ball = Ball()
score = Scoreboard()

screen.onkey(key=PLAYER1_UP_KEY, fun=p1_paddle.move_up)
screen.onkey(key=PLAYER1_DOWN_KEY, fun=p1_paddle.move_down)

screen.onkey(key=PLAYER2_UP_KEY, fun=p2_paddle.move_up)
screen.onkey(key=PLAYER2_DOWN_KEY, fun=p2_paddle.move_down)

while game_on:
    print(ball.ball_speed)
    time.sleep(SCREEN_TIME_REFRESH)
    screen.update()
    ball.move()

    if ball.ycor() >= 280:
        ball.bounce_down()
    elif ball.ycor() <= -280:
        ball.bounce_up()

    if ball.distance(p2_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_paddle(ball.xcor())
    elif ball.distance(p1_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_paddle(ball.xcor())

    if ball.xcor() >= 410 or ball.xcor() <= -410:
        score.add_score(ball.xcor())
        ball.reset(ball.xcor())
        

screen.exitonclick()