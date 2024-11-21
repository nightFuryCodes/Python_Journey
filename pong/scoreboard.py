from turtle import Turtle


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(position)
        self.write(f"{self.score}", align='center', font=('Arial', 24, 'normal'))
        self.hideturtle()

    def increase(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", align='center', font=('Arial', 24, 'normal'))

