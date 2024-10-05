import turtle as tur
import colorsys as cs

# Setup turtle environment
tur.speed(0)
tur.bgcolor('black')
tur.width(2)

# Draw 5-point star with RGB color transitions
for i in range(360):
    color = cs.hsv_to_rgb(i / 360, 1, 1)  # HSV to RGB color transition
    tur.color(color)

    # Draw a 5-point star
    for j in range(5):
        tur.forward(200)
        tur.right(144)  # Angle for a 5-point star

    tur.right(10)  # Slightly rotate after each star for a rotating effect

tur.done()




