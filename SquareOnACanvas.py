import turtle
turtle.Screen().bgcolor("Red")
screen = turtle.Screen()
screen.setup(600,400)

pen = turtle.Turtle()

for i in range(4):
    pen.forward(100)
    pen.left(90)
    i=i+1
    
turtle.done()