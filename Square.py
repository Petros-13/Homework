import turtle
screen = turtle.Screen()
screen.title("Dharani's Turtle Square Project")
screen.bgcolor("lightblue")  # Change background colour here
pen = turtle.Turtle()
pen.pensize(3)
pen.speed(3)
pen.color("purple")
for _ in range(4):
    pen.forward(100)
    pen.right(90)
turtle.done()
