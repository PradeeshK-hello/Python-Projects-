import turtle
turtle.Screen().bgcolor("White")
screen = turtle.Screen()
screen.setup(440,320)

pen = turtle.Turtle()

for i in range(3):
    pen.color("Blue")
    pen.forward(66)
    pen.right(120)
    i=i+1

pen.penup()
pen.right(90)
pen.forward(40)
pen.right(90)
pen.pendown()

for j in range(3):
    pen.color("Blue")
    pen.back(66)
    pen.left(120)
    i=i+1
    
turtle.done()