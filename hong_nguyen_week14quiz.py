# Design a function that accepts a list of numbers as an argument. The function should recursively
# calculate the sum of all the numbers in the list and return that value. Write the main program to
# test the function , which will input from the key board.
#
# Write the comments for each statement.
#
# Submit the screenshot with source code and output, Also upload the source code for these programs

# Prompt the user to enter how many numbers they want to input
count = int(input("How many numbers? "))

# Create an empty list to store the numbers entered by the user
numbers = []

# Use a for loop to get 'count' numbers from the user
for i in range(count):
    # Prompt the user to enter a number, then convert the input string to an integer
    value = int(input("Enter a number: "))
    # Append the entered number to the list of numbers
    numbers.append(value)

# Define a recursive function that calculates the sum of the numbers in a list
def sumRecursive(num_list: list[int]) -> int:
    # Base case: if the list is empty, the sum is 0
    if len(num_list) == 0:
        return 0

    # Store the first number in the list
    firstNum = num_list[0]

    # Recursively calculate the sum of the remaining numbers in the list
    # and add it to the first number
    return firstNum + sumRecursive(num_list[1:])

# Call the recursive function with the list of numbers and print the result
print(sumRecursive(numbers))