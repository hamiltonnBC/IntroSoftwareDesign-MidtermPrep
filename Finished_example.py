#####################################################
#
# REVIEW THIS AFTER YOU HAVE ATTEMPTED THE EXERCISES
# Happy coding! :)
#
#####################################################

import turtle

def draw_circle(t, sz):
    """Draws a circle with the given turtle and size."""
    t.circle(sz)  # Draws a circle with the radius sz


def draw_square(t, size):
    """Draws a square of a given size."""
    for side in range(4):  # For loop to draw each side of the square
        t.forward(size)
        t.right(90)


def main():
    wn = turtle.Screen()  # Set up the Turtle window
    wn.bgcolor("lightblue")  # Set the background color

    # Create a turtle object for the circle
    circle_turtle = turtle.Turtle()
    circle_turtle.speed(0)  # Set the drawing speed to the fastest
    circle_size = 100
    draw_circle(circle_turtle, circle_size)  # Draw a circle with the specified size

    # Create a turtle for drawing squares
    square_turtle = turtle.Turtle()
    square_turtle.speed(0)  # Set the drawing speed to the fastest
    size = 100  # Initial size of the square

    # While loop to draw squares and decrease their size
    while size > 20:
        if size > 75:
            square_turtle.color("blue")
        elif size > 50:
            square_turtle.color("green")
        else:
            square_turtle.color("red")

        draw_square(square_turtle, size)  # Draw a square of the current size

        square_turtle.penup()
        square_turtle.right(10)  # Rotate slightly to the right for the spiral effect
        square_turtle.forward(10)  # Move a bit forward to start the next square
        square_turtle.pendown()

        size -= 10  # Decrease the size for the next square

    wn.exitonclick()  # Wait for a user click to close the window


if __name__ == "__main__":
    main()
