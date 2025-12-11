# Write a recursive function that accepts an integer argument, n.
# The function should display n lines of asterisks on the screen,
# with the first line showing 1 asterisk, the second line showing
# 2 asterisks, up to the nth line which shows n asterisks. Demonstrate
# the function in a main python program.  Write the comment for each statement.
# Compile and Run the program and upload the screenshot of code
# with output and programming code

# Define the recursive function that accepts an integer n and prints n lines of asterisks
def print_asterisks(n):
    # Check if n is greater than 0 to continue recursion
    if n > 0:
        # Make a recursive call with n-1 to handle the previous lines
        print_asterisks(n - 1)
        # Print a line with n asterisks
        print("*" * n)

# Call the recursive function to display the asterisks
print_asterisks(5)

# Many financial experts advise that property owners should insure their homes
# or buildings for at least 80 percent of the amount it would cost to replace
# the structure. Write a python function replacement_cost that will calculate
# and display the minimum amount of insurance he or she should buy for the property.
# The write a test program that will call  to function, so that user can input
# the amount data from the key board. Write the comment for each statement.
# Compile and Run the program and upload the screenshot of code with
# output and programming code

# Define the function to calculate and display the minimum insurance amount
def replacement_cost(cost):
    # Calculate 80% of the replacement cost as the minimum insurance
    min_insurance = cost * 0.8
    # Display the minimum insurance amount formatted to two decimal places
    print(f"The minimum amount of insurance you should buy is ${min_insurance}")

# Prompt the user to enter the replacement cost and convert to float
cost = float(input("Enter the replacement cost of the property: "))
# Call the function with the user input
replacement_cost(cost)

# Write a program that asks the user for the name of a file. If that file does
# not exist, it should display exception error message. The program should
# display only the first five lines of the file’s contents. If the file contains
# less than five lines, it should display the file’s entire contents. Write the
# comment for each statement. Compile and Run the program and upload the screenshot
# of code with output and programming code

# Import the os module to check if the file exists
import os

# Ask the user for the filename
filename = input("Enter the name of the file: ")

# Check if the file exists using os.path.exists
if not os.path.exists(filename):
    # If the file does not exist, display an error message
    print("Error: The file does not exist.")
else:
    # If the file exists, try to open and read it
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read all lines from the file
            # Turn into a list, each element is each line in the text files
            lines = file.readlines()

            # Determine how many lines to display (up to 5)
            num_lines = min(5, len(lines))

            # Loop through and print the first num_lines
            for i in range(num_lines):
                # Print each line, stripping the newline character
                print(lines[i], end="")

            print("...")
    # Catch any exceptions that occur during file reading
    except Exception as e:
        # Display the exception error message
        print(f"An error occurred while reading the file: {e}")

# Knowing that (x + 1)^2 = x^2 + 2x + 1, and that multiplication is
# more time consuming than addition, write an efficient python program
# that displays the first ten natural numbers and their squares. Write
# the comment for each statement. Compile and Run the program and upload
# the screenshot of code with output and programming code

# Initialize x to 1 (first natural number)
x = 1
# Initialize square to 1 (square of 1)
square = 1
# Display the first natural number and its square
print(f"{x} {square}")
# Loop from 2 to 10 to calculate and display the next numbers and squares
for i in range(2, 11):
    # Update square using the efficient formula: square += 2*x + 1
    square += 2 * x + 1
    # Increment x to the next natural number
    x += 1
    # Display the current natural number and its square
    print(f"{x} {square}")



# Design a recursive function named multiply that accepts two arguments into
# parameters x and y. The function should return the product of x times y.
#
# Hint: Recall that multiplication can be performed as repeated addition.
# (Keep it simple, assume x and y will always hold nonnegative integers).

# Define the recursive function to multiply two nonnegative integers using repeated addition
def multiply(x, y):
    # Base case: if y is 0, the product is 0
    if y == 0:
        return 0
    # Recursive case: add x to the product of x and (y-1)
    return x + multiply(x, y - 1)

print(multiply(2,3))

from random import randint

num = randint(0,100)
print(num)

