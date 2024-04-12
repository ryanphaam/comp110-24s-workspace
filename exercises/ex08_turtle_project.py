"""TODO: Describe your scene program."""
 
__author__ = "730710909"
 
from turtle import Turtle, colormode, done

colormode(255)


def main() -> None:
    """Main function combining all functions."""
    ertle: Turtle = Turtle()
    colors: list[str] = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
    draw_background(ertle, -1000, 0)
    draw_background(ertle, -1000, -1000)
    draw_white_ray(ertle, 0, -10)
    draw_rainbow(ertle, colors, 0, 2)
    draw_outline(ertle, -150, -100)
    done()


def draw_background(a_turtle: Turtle, x: float, y: float) -> None:
    """Set up background for the picture."""
    a_turtle.speed(100)
    a_turtle.pencolor("black")
    a_turtle.fillcolor(0, 0, 0)
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.begin_fill()
    i: int = 0
    while (i < 4):
        a_turtle.forward(100000000)
        a_turtle.left(90)
        i += 1
    a_turtle.end_fill()
    a_turtle.hideturtle()


def draw_outline(a_turtle: Turtle, x: float, y: float) -> None:
    """Drawing prism (triangle)."""
    a_turtle.speed(25)
    a_turtle.pencolor("white")
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.begin_fill()
    a_turtle.fillcolor(0, 0, 0)
    i: int = 0
    while (i < 3):
        a_turtle.forward(300)
        a_turtle.left(120)
        i += 1
    a_turtle.end_fill()
    a_turtle.hideturtle()


def draw_white_ray(a_turtle: Turtle, x: int, y: int) -> None:
    """Drawing white ray with rectangle."""
    a_turtle.speed(100)
    a_turtle.pencolor("black")
    a_turtle.penup()
    a_turtle.goto(x, y)
    a_turtle.pendown()
    a_turtle.begin_fill()
    a_turtle.fillcolor("white")
    i: int = 0
    while (i < 2):
        a_turtle.forward(300)
        a_turtle.left(90)
        a_turtle.forward(100)
        a_turtle.left(90)
        i += 1
    a_turtle.end_fill()
    a_turtle.hideturtle()


def draw_rainbow(a_turtle: Turtle, colors: list[str], index: int, y: float) -> None:
    """Drawing Pink Floyd's rainbow."""
    if index > len(colors) - 1:
        return
    else:
        a_turtle.speed(100)
        a_turtle.pencolor(colors[index])
        a_turtle.penup()
        a_turtle.goto(-180, y * -25)
        a_turtle.pendown()
        a_turtle.begin_fill()
        a_turtle.fillcolor(colors[index])
        i: int = 0
        while (i < 4):
            a_turtle.forward(165)
            a_turtle.left(90)
            i += 1
        a_turtle.end_fill()
        a_turtle.hideturtle()
        draw_rainbow(a_turtle, colors, index + 1, y + 1)


if __name__ == "__main__":
    main()