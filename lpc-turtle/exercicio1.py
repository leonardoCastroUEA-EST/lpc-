# Python program for Plotting Fibonacci
# spiral fractal using Turtle
import turtle
import math


def plot_fibonacci(n):

    first_number = 0
    second_number = 1
    square_first = first_number
    square_second = second_number

    # Setting the colour of the plotting pen to blue
    x.pencolor("blue")

    # Drawing the first square
    x.forward(second_number * factor)
    x.left(90)
    x.forward(second_number * factor)
    x.left(90)
    x.forward(second_number * factor)
    x.left(90)
    x.forward(second_number * factor)

    # Proceeding in the Fibonacci Series
    temp = square_second
    square_second = square_second + square_first
    square_first = temp

    # Drawing the rest of the squares

    for i in range(1, n):

        x.backward(square_first * factor)
        x.right(90)
        x.forward(square_second * factor)
        x.left(90)
        x.forward(square_second * factor)
        x.left(90)
        x.forward(square_second * factor)

        # Proceeding in the Fibonacci Series
        temp = square_second
        square_second = square_second + square_first
        square_first = temp

    # Bringing the pen to starting point of the spiral plot
    x.penup()
    x.setposition(factor, 0)
    x.seth(0)
    x.pendown()

    # Setting the colour of the plotting pen to red
    x.pencolor("red")

    # Fibonacci Spiral Plot
    x.left(90)

    for i in range(n):

        print(second_number)
        fdwd = math.pi * second_number * factor / 2
        fdwd /= 90

        for j in range(90):

            x.forward(fdwd)
            x.left(1)
        temp = first_number
        first_number = second_number
        second_number = temp + second_number


# Here 'factor' signifies the multiplicative
# factor which expands or shrinks the scale
# of the plot by a certain factor.
factor = 1

# Taking Input for the number of
# Iterations our Algorithm will run
n = int(input('Enter the number of iterations (must be > 1): '))

# Plotting the Fibonacci Spiral Fractal
# and printing the corresponding Fibonacci Number

if n > 0:

    print("Fibonacci series for", n, "elements :")
    x = turtle.Turtle()
    x.speed(100)
    plot_fibonacci(n)
    turtle.done()

else:

    print("Number of iterations must be > 0")
