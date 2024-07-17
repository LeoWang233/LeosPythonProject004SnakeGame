# main.py

# import
import time
from turtle import Screen
from border import Border
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# 屏幕初始化
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

# 全部项目初始化
border = Border()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# 采集键盘内容
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

# 游戏主程序
game_is_on = True
while game_is_on:

    # 蛇的移动
    screen.update()
    time.sleep(0.15)
    snake.move()

    # 撞上食物
    if snake.head.distance(food) <= 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # 撞上边缘
    if snake.head.xcor() > 400 or snake.head.xcor() < -400 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False
        scoreboard.game_over()

    # 撞上尾巴
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 15:
            game_is_on = False
            scoreboard.game_over()

# 屏幕关闭标记
screen.exitonclick()
