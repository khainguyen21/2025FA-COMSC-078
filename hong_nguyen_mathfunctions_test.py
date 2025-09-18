# Hong Nguyen and description of the purpose of the program go here.

# Statistical Functions Program
# This program implements four mathematical functions: reciprocal, mean,
# geometric_mean, and harmonic_mean.

import math

def reciprocal(number):
    """Return the reciprocal of a number (1/number)."""
    return 1 / number

def mean(a, b, c):
    """Return the arithmetic mean (average) of three numbers."""
    return (a + b + c) / 3

def geometric_mean(a, b, c):
    """Return the geometric mean of three numbers.
    The geometric mean is the cube root of the product of the numbers."""
    return math.pow(a * b * c, 1/3)

def harmonic_mean(a, b, c):
    """Return the harmonic mean of three numbers.
    The harmonic mean is the reciprocal of the mean of the reciprocals."""
    return reciprocal(mean(reciprocal(a), reciprocal(b), reciprocal(c)))


# this code goes AFTER your functions.

def main():
    print("Reciprocal of 8 is", reciprocal(8), "[should be 0.125]")
    print("Reciprocal of 4/3 is", reciprocal(4/3), "[should be 0.75]")
    print("Reciprocal of -3 is", reciprocal(-3), "[should be -0.3333...]")

    print("Mean of 1, 13, 4 is", mean(1, 13, 4), "[should be 6.0]")
    print("Mean of -5, -12, -9 is", mean(-5, -12, -9), "[should be -8.666...]")

    print("Geometric mean of 144, 2, 6 is", geometric_mean(144, 2, 6),
          "[should be 11.9999..]")
    print("Geometric mean of 2.1, 16.8, 16.8 is", geometric_mean(2.1, 16.8, 16.8),
          "[should be 8.3.999...]")

    print("Harmonic mean of 1, 2, 3 is", harmonic_mean(1, 2, 3),
          "[should be 1.636363...]")
    print("Harmonic mean of -2, 1, 1 is", harmonic_mean(-2, 1, 1),
          "[should be 2.0]")

main()
