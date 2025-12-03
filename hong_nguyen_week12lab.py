from fractions import Fraction


def readInt():
    """
    Simple function to read an integer with exception handling.
    """
    try:
        intVal = int(input('Enter an integer value: '))
        print('The square of the number you entered is: ', intVal**2)
    except ValueError:
        print('Error: The value entered was not an integer.')


def readVal(valType, promptMsg, errorMsg):
    """
    General function to read any type of input with exception handling.
    
    Parameters:
    - valType: The type to convert the input to (e.g., int, float, Fraction, complex)
    - promptMsg: The message to display when prompting for input
    - errorMsg: The error message to display if conversion fails
    
    Returns:
    - The converted value if successful, or None if conversion fails
    """
    try:
        userInput = input(promptMsg + ': ')
        value = valType(userInput)
        return value
    except (ValueError, TypeError) as e:
        print(f"Error: '{userInput}' {errorMsg}")
        return None


def main():
    """
    Driver program to test readVal with different types.
    """
    print("Testing readVal with different types:\n")
    
    # Test with integer
    print("--- Testing Integer ---")
    val = readVal(int, 'Enter an integer', 'is not an integer')
    if val is not None:
        print(f"Successfully read integer: {val}")
        print(f"The square is: {val**2}\n")
    else:
        print()
    
    # Test with float
    print("--- Testing Float ---")
    val = readVal(float, 'Enter a float', 'is not a float')
    if val is not None:
        print(f"Successfully read float: {val}")
        print(f"The square is: {val**2}\n")
    else:
        print()
    
    # Test with Fraction
    print("--- Testing Fraction ---")
    val = readVal(Fraction, 'Enter a fraction (e.g., 1/2)', 'is not a valid fraction')
    if val is not None:
        print(f"Successfully read fraction: {val}")
        print(f"The square is: {val**2}\n")
    else:
        print()
    
    # Test with Complex
    print("--- Testing Complex ---")
    val = readVal(complex, 'Enter a complex number (e.g., 1+2j)', 'is not a complex number')
    if val is not None:
        print(f"Successfully read complex number: {val}")
        print(f"The square is: {val**2}\n")
    else:
        print()


if __name__ == "__main__":
    main()