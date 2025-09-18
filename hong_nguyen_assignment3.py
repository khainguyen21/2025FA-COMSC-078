import math

def summation (f, lower, upper):
    total = 0
    for i in range(lower, upper + 1):
        total += f(i)
    return total


def square(x):
    """ This function calculates and returns the square of the input argument x """
    return x ** 2
def fourth_power(x):
    """ This function calculates and returns the fourth power of x.
    It uses neither x*x*x*x, x**4, nor math.pow(x, 4) """
    return x ** 4

print("User Input: ")
lower = int(input("Enter a lower bound for the sum: "))
upper = int(input("Enter an upper bound for the sum: "))

print(f"\nProgram Output: ")
print(f"The sum of squares of the numbers from {lower} to {upper} is {summation(square, lower, upper)}")
print(f"The sum of the fourth powers of the numbers {lower} to {upper} is {summation(fourth_power, lower, upper)}")
print(f"The sum of square roots of the numbers from {lower} to {upper} is {summation(lambda x : math.sqrt(x), lower, upper)}")








