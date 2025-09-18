def display_em(lower, upper):
    """ This recursive function displays the consecutive integers
    from its lower to its upper bounds """
    if lower == upper + 1:
        return 0

    print(lower)
    display_em(lower + 1, upper)
    return None


def add_em(lower, upper):
    """ This recursive function calculates the sum of the consecutive
    integers from its lower to its upper bounds"""
    if lower == upper + 1:
        return 0

    return lower + add_em(lower + 1, upper)


def applyToEach(f, lower_bound, upper_bound):
    """ This higher-order function applies the included function
    to its lower and upper bound arguments"""
    return f(lower_bound, upper_bound)

lower = int(input("Enter a lower bound: "))
upper = int(input("Enter a upper bound: "))

print()
print("The consecutive integers:")
applyToEach(display_em, lower, upper)

print()
total = applyToEach(add_em, lower, upper)
print(f"Add up to {total}")
