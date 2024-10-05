import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
t.width(3)
t.speed(25)

# Color sequence
col = ('red', 'yellow', 'green')

# Drawing rectangular spiral
for i in range(200):  # Adjusted the loop count for better visualization
    t.pencolor(col[i % 3])
    t.forward(i * 4)  # Move forward with increasing distance
    t.right(90)  # Turn 90 degrees for rectangle

# End drawing
turtle.done()
