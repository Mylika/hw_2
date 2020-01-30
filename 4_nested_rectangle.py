import turtle


def nested():
    for i in range(1, 11):
        turtle.shape('turtle')
        turtle.forward(i * 10)
        turtle.left(90)
        turtle.forward(i * 10)
        turtle.left(90)
        turtle.forward(i * 10)
        turtle.left(90)
        turtle.forward(i * 10)
        turtle.penup()
        turtle.right(90)
        turtle.forward(5)
        turtle.right(180)
        turtle.forward(5)
        turtle.pendown()


if __name__ == "__main__":
    nested()
