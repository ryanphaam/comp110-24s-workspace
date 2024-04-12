"""Turtle tutorial gameplay."""

from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

leo.speed(25)
leo.pencolor("blue")
leo.fillcolor(100, 10, 100)
leo.penup()
leo.goto(-150, -100)
leo.pendown()
leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()
leo.hideturtle()


bob: Turtle = Turtle()
bob.speed(100)
bob.pencolor("grey")
bob.fillcolor(100, 100, 100)
bob.penup()
bob.goto(-150, -100)
bob.pendown()
bob.begin_fill()
side_length: int = 300
i: int = 0
while (i < 100):
    bob.forward(side_length)
    bob.left(120)
    side_length = side_length * 0.97
    i = i + 1
bob.end_fill()
bob.hideturtle()
done()


