

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.high_score = 0
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align='center', font=('Arial', 24, 'normal'))
        self.hideturtle()

    def new_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align='center', font=('Arial', 24, 'normal'))


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.new_score()


    def increase_score(self):
        self.score += 1
        self.new_score()




