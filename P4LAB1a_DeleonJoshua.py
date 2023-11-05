# CTI-110
# P4LAB1a
# Deleon_Joshua
# 05 NOV 2023

import turtle
wn = turtle.Screen()
wn.bgcolor("red")
wn.title("make a shape Mel")

#turtle body, color, and line size
mel = turtle.Turtle()
mel.color("blue")
mel.pensize(4)
mel.shape("turtle")
# mel draws a square
for a in range(4):
    mel.forward(200)
    mel.left(90)
# mel draws a triangle
for b in range(3):
    mel.forward(50)
    mel.left(120)
    
wn.mainloop()
