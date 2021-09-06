from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 24, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score = {self.score}", align=ALIGN, font=FONT)
        self.hideturtle()


    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", align="center", font=("Courier", 24, "normal"))


    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 24, "normal"))
