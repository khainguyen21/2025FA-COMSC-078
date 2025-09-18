def to_decimal(degrees, minutes, seconds):
    """
    Convert degrees, minutes, and seconds to decimal degrees.
    
    Parameters:
    degrees -- the degree component (can be negative)
    minutes -- the minute component (will be converted to positive)
    seconds -- the second component (will be converted to positive)
    
    Returns:
    A decimal degree value
    """
    # Ensure degrees is an integer
    degrees = int(degrees)
    
    # Ensure minutes is a positive integer
    minutes = abs(int(minutes))
    
    # Ensure seconds is positive
    seconds = abs(float(seconds))

    # Convert everything into seconds
    total_seconds = abs(degrees) * 3600 + minutes * 60 + seconds

    # Convert back to decimal degrees
    decimal = total_seconds / 3600

    # Take the negative sign if decimal is less than 0
    if degrees < 0:
        decimal = -decimal

    return decimal

def main():
    # Get input from the user
    degrees = input("Enter degrees: ")
    minutes = input("Enter minutes: ")
    seconds = input("Enter seconds: ")
    
    # Convert string inputs to appropriate numeric types
    decimal_degrees = to_decimal(degrees, minutes, seconds)
    
    # Display the result
    print(f"That is {decimal_degrees} decimal degrees.")

main()