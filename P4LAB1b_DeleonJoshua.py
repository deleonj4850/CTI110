# CTI-110
# P4LAB1b
# Deleon_Joshua
# 05 NOV 2023

import turtle
wn = turtle.Screen()
wn.bgcolor("green")
wn.title("Draw initials Mel")

#turtle body, color, and line size
mel = turtle.Turtle()
mel.color("purple")
mel.pensize(5)
mel.shape("turtle")
# mel draws a J
mel.penup()
mel.backward(300)
mel.pendown()
mel.left(90)
mel.forward(40)
mel.left(180)
mel.forward(40)
mel.left(90)
mel.forward(60)
mel.left(90)
mel.forward(120)
# mel draws a D
mel.penup()
mel.left(180)
mel.forward(120)
mel.left(90)
mel.forward(80)
mel.left(90)
mel.pendown()
mel.forward(120)
mel.left(180)
mel.forward(120)
mel.left(90)
mel.forward(50)
mel.left(50)
mel.forward(40)
mel.left(40)
mel.forward(55)
mel.left(40)
mel.forward(40)
mel.left(50)
mel.forward(50)

    
wn.mainloop()
