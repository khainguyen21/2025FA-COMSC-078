# Question 1
# Import random to a library to generate a random number
import random

# Check if the number is even -> True or odd -> False
def is_even(num: int) -> bool:
    if num % 2 == 0:
        return True
    else :
        return False

# Keep asking user if they want to re-run the whole program until they input n
while True:
    # Use hash table to store numbers of odd num and even num
    record = {'Odd': 0, 'Even': 0}

    # Loop for 100 times for 100 random numbers
    for i in range(0, 100):

        # Generate random number
        currentNumber = random.randint(1, 1000000)

        # Check if the number is even or odd, then update its value in a hashtable
        if is_even(currentNumber):
            record['Even'] += 1
        else:
            record['Odd'] += 1

    # Print out the result
    print(f"Out of 100 random numbers, {record['Odd']} were odd, and {record['Even']} were even.")

    # Ask your user if they want to re-run
    user_input = input("Would you like to run the program again (Y/N): ")

    # If input from the user is equal not y, then break the loop
    if user_input.lower() != 'y':
        break

# Question 2

def getSmallest(numbers: list[int]) -> int:
    # Assign the first number in the list to be the smallest
    smallest = numbers[0]

    # Iterate through the list for the smallest number
    for num in numbers:
        if num < smallest:
            smallest = num

    return smallest

# Initialize the list
list_numbers = []
# Initialize the counter
total_num = 1

while total_num <= 10:
    user_input = int(input(f"Please enter your number to the list ({total_num} of 10): "))
    total_num += 1
    list_numbers.append(user_input)

print(f"The smallest number from the list that you just type: {getSmallest(list_numbers)}")




