#create paddle
from turtle import Turtle,Screen

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.y=0
        #self.list=[]
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

        # self.paddle()
    # def paddle(self):
    #     #create paddle
    #     for _ in range(2):
    #         paddles=Turtle(shape="square")
    #         paddles.color("white")
    #
    #         paddles.penup()
    #         paddles.turtlesize(stretch_wid=5, stretch_len=1)
    #         self.list.append(paddles)

    # def right_p(self):
    #     #list[0] is right paddle
    #      self.list[0].goto(350,0)
    #
    # def left_p(self):
    #     self.list[1].goto(-350,0)

    def up(self):
      #move up
       self.y+=20
       self.goto(350,self.y)
    def down(self):
        #move down
        self.y -= 20
        self.goto(350,self.y)

    def l_up(self):
        self.y+=20
        self.goto(-350,self.y)
    def l_down(self):
        self.y-=20
        self.goto(-350,self.y)



