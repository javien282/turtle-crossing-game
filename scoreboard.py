from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.score_board()


    def score_board(self):
        self.hideturtle()
        self.setpos(-200, 250)
        self.color("black")
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def add_point(self):
        self.level += 1
        self.clear()
        self.score_board()

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)

