"""
Run `python3 example.py` to draw a square using turtle graphics.
"""

import turtle
from time import sleep

# Create a turtle object
# A turtle object is used to draw on the screen. No onwards whatever 
# actions are called on this object will be reflected on the screen.
my_turtle = turtle.Turtle()

# with 140 this should be 18 to come back to same spot.
# with 135 this should be 8 to come back to same spot.
# with 162 this should be 20 to come back to same spot.
# ( 180 - 162 ) * 20 = 360
k: int = 12
# Draw an equilateral shape with k sides
for i in range(k):
    # print("Current value of i is: ", i)
    my_turtle.forward(100)
    my_turtle.right(180 - 360/k)
    sleep(1)

# Keep the window open. If you uncomment the line below you will see
# the window closing immediately after the square is drawn.
# With the line below, the window will close only when you click on the
# close button and the command will only terminate after that.
turtle.done()
