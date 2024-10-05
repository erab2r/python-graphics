from turtle import *

# Setup for turtle
tracer(3)  # Set turtle speed
bgcolor('black')  # Background color
pensize(2)

# List of colors to cycle through
colors = ['red', 'green', 'yellow', 'violet']

# Drawing pattern
for i in range(200):
    color(colors[i % 4])  # Cycle through red, green, yellow, and violet

    circle(200 - i, 90)  # Create a circular arc, reducing radius as i increases
    left(90)  # Turn left by 90 degrees
    left(20)  # Turn left by 20 degrees
    circle(200 - i, 90)  # Create another circular arc
    left(18)  # Turn left by 18 degrees

done()
