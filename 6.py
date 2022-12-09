import turtle
k = 60
turtle.speed(0)
turtle.tracer(0, 0)
for i in range(7):
    turtle.forward(10 * k)
    turtle.right(120)
turtle.setposition(0, 0)
turtle.penup()
for x in range(15):
    for y in range(-15, 5):
        turtle.setposition(x*k, y*k)
        turtle.dot(5, "red")
turtle.update()
turtle.done()