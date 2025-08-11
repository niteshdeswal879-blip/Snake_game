from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score= 0
        with open("data.txt", "r") as file:
            self.highscore= file.read()
        self.color("White")
        self.penup()
        self.goto(0,270)
        self.write(f"Scoreboard: {self.score}  Highscore: {self.highscore}" ,False,"center",("Arial",15, "normal" ))
        self.hideturtle()

    def increase(self):
        self.score+=1
        self.update()
    def reset(self):
        if self.score > int(self.highscore):
            self.highscore=self.score
            with open("data.txt","w") as file:
                file.write(str(self.highscore))
        self.score=0
        self.update()

    def update(self):
        self.clear()
        self.write(f"Scoreboard: {self.score} Highscore: {self.highscore}", False, "center", ("Arial", 15, "normal"))




