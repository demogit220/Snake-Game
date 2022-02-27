from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self,screen):
        super().__init__()
        self.score = 0
        self.user_name = screen.textinput(title="Name", prompt="What's your name:  ")
        with open("data.txt") as data:
            for line in data:
                for word in line:
                    if word.isdigit():
                        self.high_score = int(word)
                        break
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()  # this hides the small arrow on the screen

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score Board : {self.score} High Score: {self.high_score}", align="center", font=("Arial", 16, "normal"))

    def Reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.user_name}: {self.high_score}")
        self.score=0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over!", align="center", font=("Arial", 16, "normal"))

    def update(self):
        self.score += 1
        self.update_scoreboard()
