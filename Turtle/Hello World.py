from turtle import *
from letters import *

# s = Screen()
t = Turtle()
#x = 768
#half = 384
#y = 768

H(t)
bottomSpace(t)
E(t)
bottomSpace(t)
L(t)
bottomSpace(t)
L(t)
bottomSpace(t)
O(t)

# Move the turtle to below the H to write the second word
t.penup()
t.goto(0, -30)
t.setheading(0)
t.pendown()

W(t)
rightSpace(t)
O(t)
topSpace(t)
R(t)
bottomSpace(t)
L(t)
rightSpace(t)
D(t)
