from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move=10

        self.y_move=10
        self.i = 1
    def move(self):
        self.x=self.xcor()+self.x_move
        self.y=self.ycor()+self.y_move
        self.goto(self.x,self.y)

    def y_bounce(self):
    #very imp mtlb jb ycor>290 xcor() bdhna chahiye or yinc ki jgha dec hone chaiye
        self.y_move*=-1

    def x_bounce(self):
        self.x_move*=-1
    def reset(self):
        #after loosing point ball started moving from opposite play
        self.goto(0,0)
        self.x_bounce()

