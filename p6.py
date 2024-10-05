import turtle
import random

def draw_circle(color, radius, x, y):
    """Draws a filled circle with the specified color, radius, and position."""
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def get_random_color():
    """Returns a random RGB color."""
    return (random.random(), random.random(), random.random())

def draw_panda():
    # Draw head
    draw_circle("white", 100, 0, -100)

    # Draw ears
    draw_circle(get_random_color(), 30, -70, 20)   # Left ear
    draw_circle(get_random_color(), 30, 70, 20)    # Right ear
    draw_circle("white", 15, -70, 25)   # Left inner ear
    draw_circle("white", 15, 70, 25)    # Right inner ear

    # Draw eyes
    draw_circle(get_random_color(), 15, -35, -40)   # Left eye
    draw_circle(get_random_color(), 15, 35, -40)    # Right eye
    draw_circle("white", 7, -35, -35)    # Left eye white
    draw_circle("white", 7, 35, -35)     # Right eye white

    # Draw nose
    draw_circle(get_random_color(), 10, 0, -60)

    # Draw mouth
    turtle.penup()
    turtle.goto(0, -60)
    turtle.setheading(-60)
    turtle.pendown()
    turtle.circle(20, 120)

# Set up the turtle
turtle.speed(3)
turtle.bgcolor("lightblue")  # Optional: Set a background color

# Draw the panda
draw_panda()

# Hide turtle and finish
turtle.hideturtle()
turtle.done()
