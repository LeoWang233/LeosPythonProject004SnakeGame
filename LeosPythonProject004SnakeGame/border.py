# border.py

from turtle import Turtle


class Border(Turtle):
    """
    绘制边框
    """

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(401, 301)
        self.pendown()
        self.goto(401, -301)
        self.goto(-401, -301)
        self.goto(-401, 301)
        self.goto(401, 301)
