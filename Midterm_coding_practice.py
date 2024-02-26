######################################################################
# Authors: Nicholas Hamilton     TODO: Change this to your name
# Username: hamiltonn            TODO: Change this to your username
#
# Assignment: Reviewing software design fundamentals
#
# Purpose: To review and practice the fundamentals of software design, including
# the use of functions, conditionals, loops, and testing. This program will
# draw using the turtle graphics library.
######################################################################
# Acknowledgements:
#  Berea College Computer Science Department
######################################################################
######################################################################
# Example turtle methods: penup(), pendown(), goto(), circle(),
# hideturtle(), color(), pensize(), speed(), begin_fill(), end_fill(),
# forward(), right(), left(), backward(), fillcolor()
######################################################################
# 1 TODO: Add Docstrings to all functions
import turtle
def draw_circle(t, sz): # TODO complete this function
    # Your code here
    pass  # Remove this line when you implement the function

def draw_square(t, size): # TODO complete this function
    # Add a for loop to draw each side of the square
    pass # Remove this line when you implement the function

def main():
     # TODO: Set up Turtle Window
    # wn.bgcolor("lightblue") TODO: Change the background color to your liking.
    # TODO: Create a turtle object to pass into the draw_circle function
    circle_size = 100
    # draw_circle(#TODO: pass your turtle object and the variable circle_size here separated by a comma)
    #
    square_turtle = turtle.Turtle()  # Create a turtle for drawing square
    square_turtle.speed(0)  # Set the drawing speed to the fastest
    size = 100

    # TODO: Create a While loop that runs until size is less than 20.
    # TODO: Inside the While loop, determine the color of the square when size
    # TODO: is greater than 75, greater than 50, and less than or equal to 50.
    # TODO: The draw square function code is below, and is indented to be inside of the while loop.

        draw_square(square_turtle, size) ################################################
        square_turtle.penup()           # THIS BLOCK OF CODE SHOULD BE INSIDE THE WHILE LOOP
        square_turtle.right(10)         # DO NOT EDIT
        square_turtle.forward(10)
        square_turtle.pendown()
        size -= 10  # Decrease the size for the next square ##################

    # After the while loop, add the following line undented to close the window on click.

    # TODO: Add exit on click method to close the window.

if __name__ == "__main__":
    main()
