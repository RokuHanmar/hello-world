from turtle import *

# Height of 90, width of 30

def H(t):
    t.left(90)
    t.forward(90)
    t.backward(45)
    t.right(90)
    t.forward(30)
    t.left(90)
    t.forward(45)
    t.backward(90)

def E(t):
    t.forward(30)
    t.backward(30)
    t.right(90)
    t.forward(45)
    t.left(90)
    t.forward(30)
    t.backward(30)
    t.right(90)
    t.forward(45)
    t.left(90)
    t.forward(30)
        
    
def L(t):
    t.right(90)
    t.forward(90)
    t.left(90)
    t.forward(30)

def O(t):
    t.right(90)
    t.forward(90)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(90)
    t.left(90)
    t.forward(30)
    
def W(t):
    t.right(90)
    t.forward(90)
    t.left(150)
    t.forward(45)
    t.right(130)
    t.forward(45)
    t.left(150)
    t.forward(90)

def R(t):
    t.left(90)
    t.forward(90)
    for i in range(3):
        t.right(90)
        t.forward(30)
    t.left(120)
    t.forward(70)

def D(t):
    t.left(90)
    t.forward(90)
    t.right(140)
    t.forward(70)
    t.right(95)
    t.forward(70)
    
def bottomSpace(t):
    x = t.xcor()
    y = t.ycor()
    t.penup()
    t.setheading(90) # faces up
    t.forward(90)
    t.setheading(0) # faces right
    t.forward(10)
    t.pendown()

def topSpace(t):
    t.penup()
    t.setheading(270) # faces down
    t.forward(90)
    t.setheading(0) # faces right
    t.forward(40)
    t.setheading(0)
    t.pendown()

def rightSpace(t):
    t.penup()
    t.setheading(0)
    t.forward(10)
    t.pendown()
