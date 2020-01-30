def golden_ratio():  # 1.61803398875
    import turtle
    t = turtle.Turtle()
    t.width(3)
    t.color('#9c20ff')
    t.shapesize(0.1)
    t.penup()
    t.backward(350)
    t.left(90)
    t.backward(320)
    t.hideturtle()
    t.pendown()
    t.right(180)
    x, y, speed = 450, -90, 30
    for n in range(30):
        t.circle(x, y, speed)
        x = x / 2
        speed = speed - 1
