
from turtle import Turtle
import multiprocessing
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update_score()

        #note: single turtle can wite diff things at diff location
    def update_score(self):
        #imp to make this fun seprately to keep both teams score on screen
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("courier", 80, "normal"))

    def l_point(self):
          self.clear()
          self.l_score += 1
          self.update_score()
    def r_point(self):
        self.clear()
        self.r_score += 1
        self.update_score()
