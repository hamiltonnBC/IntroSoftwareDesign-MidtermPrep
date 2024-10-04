######################################################################
# Authors: Jane Doe
# Username: doej
#
# Assignment: Reviewing software design fundamentals
#
# Purpose: To review and practice the fundamentals of software design, including
# the use of functions, conditionals, loops, and testing. This program will
# draw using the turtle graphics library.
######################################################################
# Acknowledgements:
#  Berea College Computer Science Department
#  Original Author: Nicholas Hamilton
######################################################################

import turtle


def draw_circle(t, sz):
    """
    Draw a circle using the given turtle and size.

    Args:
        t (turtle.Turtle): The turtle object to use for drawing.
        sz (int): The size (radius) of the circle.
    """
    t.circle(sz)


def draw_square(t, size):
    """
    Draw a square using the given turtle and size.

    Args:
        t (turtle.Turtle): The turtle object to use for drawing.
        size (int): The size (side length) of the square.
    """
    for i in range(4):
        t.forward(size)
        t.right(90)


def main():
    # Set up Turtle Window
    wn = turtle.Screen()
    wn.bgcolor("lightblue")

    # Create a turtle object for drawing circles
    circle_turtle = turtle.Turtle()
    circle_turtle.speed(0)
    circle_size = 100
    draw_circle(circle_turtle, circle_size)

    # Create a turtle for drawing squares
    square_turtle = turtle.Turtle()
    square_turtle.speed(0)  # Set the drawing speed to the fastest
    size = 100

    # Implement the while loop to draw squares
    while size >= 20:
        # Set color based on size
        if size > 75:
            square_turtle.color("red")
        elif size > 50:
            square_turtle.color("green")
        else:
            square_turtle.color("blue")

        # Draw the square
        draw_square(square_turtle, size)

        # Move turtle and prepare for next square
        square_turtle.penup()
        square_turtle.right(10)
        square_turtle.forward(10)
        square_turtle.pendown()

        # Decrease size for next square
        size -= 10

    # Add exit on click method to close the window
    wn.exitonclick()


if __name__ == "__main__":
    main()