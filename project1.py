import turtle as tur
import colorsys as cs

# First pattern
tur.speed(0)
tur.bgcolor('black')
tur.width(2)

for i in range(180):
    tur.color(cs.hsv_to_rgb(abs(90-i)/90, abs(90-i)/90, 1))
    tur.forward(100)
    tur.left(60)
    tur.forward(100)
    tur.right(120)
    tur.circle(50)
    tur.left(240)
    tur.forward(100)
    tur.left(60)
    tur.forward(100)
    tur.left(122)

# Second pattern
from turtle import *
import colorsys

tracer(2)
pensize(2)
h = 0.2
bgcolor("black")
lt(80)
fd(250)
lt(180)
lt(80)

for i in range(330):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    color(c)
    h += 0.004
    fd(i)
    rt(50)
    rt(40)
    fd(500)
    rt(120)

tur.done()