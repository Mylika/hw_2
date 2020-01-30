import turtle


def circle():
    turtle.shape('turtle')
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()
    turtle.left(90)
    for i in range(359):
        turtle.forward(1)
        turtle.right(1)

if __name__ == "__main__":
    circle()
    while True:
        pass
