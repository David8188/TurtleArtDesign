import turtle
from myShape import *
from function import *
turtle.colormode(255)

bob=turtle.Turtle()
bob.speed(0)
turtle.bgcolor("black")
bob.color("white")
bob.pendown()
turtle.tracer(0)


for times in range(255):
    bob.color(times+1,153,93)
    bob.circle(times+1)
    bob.forward(12)
    bob.left(24)

move(bob,-30,0)
for times in range(255):
    bob.color(times+1,153,93)
    triangle(bob,times+1)
    bob.forward(70)
    bob.left(120)
move(bob,20,0)
for times in range(255):
    bob.color(times+1,153,93)
    triangle(bob,times+1)
    bob.forward(times+2)
    bob.left(30)

