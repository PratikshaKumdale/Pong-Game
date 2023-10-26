from turtle import Screen
from paddle import Paddle
from ball import  Ball
from scoreboard import Score
import random
import time

#step1:create the screen
screen=Screen()
screen.tracer(0)

screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("pong")

#ball
b=Ball()
b.move()
left_paddle=Paddle((-350,0))
right_paddle=Paddle((350,0))

score = Score()


screen.listen()
#move right paddle
screen.onkey(key="Up",fun=right_paddle.up)
screen.onkey(key="Down",fun=right_paddle.down)
#move left paddle
screen.onkey(key="w",fun=left_paddle.l_up)
screen.onkey(key="s",fun=left_paddle.l_down)
i=0.1
is_on=True
while is_on:
    if i>0:
        time.sleep(i)
        screen.update()
        b.move()
    #making ball bounce
    if b.ycor()>280 or b.ycor()<-280:
         b.y_bounce()
    #collosion with both paddles
    if (b.distance(right_paddle)<50 and  b.xcor()>320) or (b.distance(left_paddle)<50 and  b.xcor()<-320):
        b.x_bounce()
        i-=0.01



    #detect  ball goes out of the bound


    if b.xcor()>350:
        b.reset()
        i=0.1# jb koi game reset hoga mtlb jb koi ek point loose krga to speed wps normal se start hogi
        score.l_point()



    if b.xcor()<-350:
        b.reset()
        i=0.1
        score.r_point()


screen.exitonclick()
#call paddle



