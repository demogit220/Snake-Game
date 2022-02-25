from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()  # this hides the small arrow on the screen

    def update_scoreboard(self):
        self.write(f"Score Board : {self.score}", align="center", font=("Arial", 16, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=("Arial", 16, "normal"))

    def update(self):
        self.score += 1
        self.clear()  # this clears the screen before writing anything else, without this, it will just keep place one
        # number on other.
        self.update_scoreboard()
