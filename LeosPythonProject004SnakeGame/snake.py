# snake.py

from turtle import Turtle

# 蛇的初始位置常量
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    """
    跟蛇有关的类
    """

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """
        初始化蛇
        """
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        """
        增加一段身体
        """
        new_segment = Turtle(shape="square")
        new_segment.color("orange")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """
        增长一段身体
        """
        self.add_segment(self.segments[-1].position())

    def move(self):
        """
        蛇的每一次移动
        """
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x, new_y)
        self.head.forward(20)

    # 根据玩家键盘上下左右执行的操作
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
