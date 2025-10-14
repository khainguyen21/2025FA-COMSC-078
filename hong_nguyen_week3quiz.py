# print("abc" * 3)
#
# point = (3, 4)
#
# person = {point : 1}
#
# print(person[point])
# nums = [1, 2, 3, 4, 5, 6]
#
#
# print([n*n for n in nums if n % 2 == 0])
#
# def hypotenuse(x, y):
#     # hide how the result is computed; expose only the interface (x, y -> number)
#     return (x**2 + y**2) ** 0.5
#
#
# def is_right_triangle(a, b, c, *, tol=1e-9):
#     sides = sorted([a, b, c])
#     return abs(hypotenuse(sides[0], sides[1]) - sides[2]) < tol
#
# is_right_triangle(3, 4, 5)
#
#
# def pass_it(x, y):
#     z = x * y
#
#     result = get_result(z)
#
#     return (result)
#
#
# def get_result(number):
#     z = number + 2
#
#     return (z)
#
#
# num1 = 3
#
# num2 = 4
#
# answer = pass_it(num1, num2)
#
# print(answer)

def power (num , expo):
    if expo - 1 == 0:
        return num
    return num * power(num, expo-1)

def multiply (x , y):
    if y == 0:
        return 0
    return x + multiply(x , y-1)

firstNum = int(input("Enter the first number: "))
secondNum = int(input("Enter the second number: "))

print(f"The product of {firstNum} times {secondNum} is {multiply(firstNum , secondNum)}")
print(f"But {firstNum} raised to the power of {secondNum} is {power(firstNum, secondNum)}")



