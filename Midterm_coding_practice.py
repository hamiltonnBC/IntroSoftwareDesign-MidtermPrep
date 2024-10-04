######################################################################
# Authors: Example    TODO: Change this to your name
# Username: Example       TODO: Change this to your username
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
# Example turtle methods: penup(), pendown(), goto(), circle(),
# hideturtle(), color(), pensize(), speed(), begin_fill(), end_fill(),
# forward(), right(), left(), backward(), fillcolor()
######################################################################
# TODO: Add Docstrings to all functions
import turtle


def draw_circle(t, sz):  # TODO complete this function
    # Your code here
    pass  # Remove this line when you implement the function


def draw_square(t, size):  # TODO complete this function
    # Add a for loop to draw each side of the square
    pass  # Remove this line when you implement the function


def main():
    # TODO: Set up Turtle Window

    # wn.bgcolor("lightblue") TODO: Change the background color to your liking.

    # TODO: Create a turtle object to pass into the draw_circle function

    circle_size = 100
    # TODO: Call draw_circle function here. Pass circle_turtle and circle_size as arguments, separated by a comma

    # Create a turtle for drawing squares
    square_turtle = turtle.Turtle()  # Create a turtle for drawing square
    square_turtle.speed(0)  # Set the drawing speed to the fastest
    size = 100

    # TODO: Implement a while loop that runs until size is less than or equal to 20
    # Inside the while loop:
    # 1. Use if-elif-else statements to set the color of the square based on its size
    # 2. Call the draw_square function
    # 3. Move the turtle to prepare for the next square
    # 4. Decrease the size for the next square
    while size >= 20:
        # TODO: Set color based on size (use if-elif-else statements)





        # TODO: Call draw_square function here


        # Move turtle and prepare for next square
        square_turtle.penup()
        square_turtle.right(10)
        square_turtle.forward(10)
        square_turtle.pendown()

        # Decrease size for next square
        size -= 10

    # TODO: Add exit on click method to close the window



if __name__ == "__main__":
    main()