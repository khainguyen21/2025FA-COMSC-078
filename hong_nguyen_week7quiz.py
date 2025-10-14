# Design and test a program that generates a seven-digit lottery number.
# The program should generate seven random numbers, each in the range of 0 through 9,
# and assign each number to a list element. (Random numbers were discussed in Chapter 5.)
# Then write another loop that displays the contents of the list.

import random

def generate_lottery_number() -> list[int]:
    """
    Generates a list of seven random digits, each from 0 to 9
    :return:
        lists: A list containing 7 random digits
    """
    # Define the number of digits for the lottery number.
    seven_digit_number = 7

    # Create an empty list to store the random digits.
    lottery_numbers = []

    print("Generating lottery numbers...")

    for i in range(seven_digit_number):
        # Generate a random integer between 0 and 9 (inclusive)
        digit = random.randint(0,9)

        # Add a random integer into a list
        lottery_numbers.append(digit)

    print("Generation complete!")
    return lottery_numbers

def display_lottery_number(lottery_numbers: list[int]) -> None:
    """
    Displays the contents of the lottery number list
    :param lottery_numbers: The list of digits to display
    """
    # This loop iterates through each number in the list and prints it.
    # The `end=' '` argument prints a space instead of a newline after each digit,
    # keeping all the numbers on the same line for better readability.
    print("\n--------------------------")
    print("And the winning number is:")

    for num in lottery_numbers:
        print(num, end=' ')

    print("\n--------------------------")

# --- Main part of the program ---
if __name__ == "__main__":

    # 1. Generate the seven-digit number.
    winning_numbers = generate_lottery_number()

    # 2. Display the generated number.
    display_lottery_number(winning_numbers)


# Design and test a program that asks the user to enter a series of 20 numbers.
# The program should store the numbers in a list and then display the following data:
# • The lowest number in the list
# • The highest number in the list
# • The total of the numbers in the list
# • The average of the numbers in the list

def get_numbers() -> list[float]:
    """
    Prompts the user to enter 20 numbers and stores them in a list.
    Includes input validation to ensure only valid numbers are accepted.

    Returns:
        list: A list containing 20 numbers entered by the user.
    """
    numbers = []
    print("Please enter 20 numbers. Press Enter after each one.")

    # Loop until we have 20 valid numbers in a list
    while len(numbers) < 20:

        # The 'try-except' block handles cases where the user enters non-numeric input.
        try:
            # Prompt for the next number, indicating the current count.
            user_input = float(input(f"Enter a number {len(numbers) + 1 } of 20: "))
            numbers.append(user_input)

        except ValueError:
            # If the input cannot be converted to a float, show an error and repeat the prompt.
            print("Invalid input. Please enter a valid number")

    return numbers

def analyze_data (numbers: list[float]) -> tuple[float, float, float, float]:
    """
    Calculates the lowest, highest, total, and average of a list of numbers.

    Args:
        numbers (list): The list of numbers to analyze.

    Returns:
        tuple: A tuple containing the lowest number, highest number, total, and average.
    """
    # Use built-in Python functions to perform the calculations

    lowest = min(numbers)
    highest = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    return lowest, highest, total, average

def display_results(lowest: float, highest: float, total: float, average: float) -> None:
    """
    Displays the analysis results in a formatted way.

    Args:
        lowest (float): The lowest number in the list.
        highest (float): The highest number in the list.
        total (float): The sum of the numbers in the list.
        average (float): The average of the numbers in the list.
    """

    print("\n--- Data Analysis ---")
    print(f"Lowest number:  {lowest}")
    print(f"Highest number: {highest}")
    print(f"Total of numbers: {total}")
    print(f"Average of numbers: {average}")
    print("---------------------")


if __name__ == "__main__":
    # 1. Get the list of 20 numbers from the user.
    user_numbers = get_numbers()

    # 2. Analyze the data to get the required statistics.
    low, high, total_sum, avg = analyze_data(user_numbers)

    # 3. Display the final results.
    display_results(low, high, total_sum, avg)