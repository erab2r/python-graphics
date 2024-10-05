import turtle

def draw_circle(color, radius, x, y):
    """Draws a filled circle with the specified color, radius, and position."""
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_smiley():
    # Draw face
    draw_circle("yellow", 100, 0, -100)

    # Draw eyes
    draw_circle("black", 10, -35, -30)   # Left eye
    draw_circle("black", 10, 35, -30)    # Right eye

    # Draw mouth
    turtle.penup()
    turtle.goto(-40, -50)  # Start position for mouth
    turtle.setheading(-60)  # Angle for the mouth arc
    turtle.pendown()
    turtle.circle(40, 120)  # Draw the mouth

# Set up the turtle
turtle.speed(3)
turtle.bgcolor("lightblue")  # Optional: Set a background color

# Draw the smiley emoji
draw_smiley()

# Hide turtle and finish
turtle.hideturtle()
turtle.done()
