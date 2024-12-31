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
    t.backward(30)
        
    
def L(t):
    right(90)
    forward(90)
    left(90)
    forward(30)

def O(t):
    for i in range(2):
        t.forward(30)
        t.right(90)
        t.forward(90)
        t.right(90)

def W(t):
    right(90)
    forward(90)
    left(150)
    forward(45)
    right(130)
    forward(45)
    left(150)
    forward(90)

def R(t):
    left(90)
    forward(90)
    for i in range(3):
        right(90)
        forward(30)
    left(120)
    forward(70)

def D(t):
    left(90)
    forward(90)
    right(140)
    forward(70)
    right(95)
    forward(70)
    
def space(t):
    t.penup()
    t.setheading(90)
    t.forward(90)
    t.setheading(0)
    t.forward(20)
    t.pendown()

