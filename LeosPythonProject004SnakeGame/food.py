# food.py

import random
from turtle import Turtle


class Food(Turtle):
    """
    跟食物有关的类
    """

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.refresh()

    def refresh(self):
        """
        刷新食物位置
        """
        random_x = random.choice(list(range(-380, 380, 20)))
        random_y = random.choice(list(range(-280, 280, 20)))
        self.goto(random_x, random_y)
