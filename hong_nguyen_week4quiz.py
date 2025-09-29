def isPrime(n):
    # Handle special cases
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check for divisibility using 6k ± 1 optimization
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

def near_prime(n):
    # Set the current to user's number
    rightPrime = n
    # Keep adding 1, if it's not a prime number
    while not isPrime(rightPrime):
        rightPrime += 1

    # Keep subtracting 1, if it's not a prime number
    leftPrime = n
    while not isPrime(leftPrime):
        leftPrime -= 1

    # Check the distance between left prime number and right number
    if n - leftPrime >= rightPrime - n:
        return rightPrime
    else:
        return leftPrime

try:
    # Ask a user for a number
    number = int(input("Enter your number to get the nearest prime number(your number needs to be above 5): "))

    # Check if the number is above 5 otherwise keep prompting again to user
    while number <= 5:
        print()
        print("Sorry your number needs to be above 5. Please try again!")
        number = int(input("Enter your number to get the nearest prime number: "))

    # Check the nearest prime number from the user's number
    nearest_prime = near_prime(number)

    # Print nearest prime number
    print(f"The nearest prime is {nearest_prime}")

except ValueError:
    # Print out the error message if the input is not numbers
    print("\nError: Invalid input. Please re-run a program and enter a valid integer! ")
