# scoreboard.py

from turtle import Turtle


class Scoreboard(Turtle):
    """
    跟分数有关的类
    """

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        更新分数版
        """
        self.write(f'Score: {self.score}', align='center', font=("Courier", 20, "normal"))

    def increase_score(self):
        """
        增加分数并更新分数版
        """
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        """
        游戏结束
        """
        self.goto(0, 0)
        self.write(f'GAME OVER', align='center', font=("Courier", 40, "normal"))
