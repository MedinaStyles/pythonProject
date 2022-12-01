# №1
number1 = int(input("enter first number:"))
number2 = int(input("enter second number:"))
number3 = int(input("enter third number:"))
result1 = number1 + number2 + number3
result2= number1 * number2 * number3

print(number1, "+", number2, "+", number3, "=", result1)
print(number1, "*", number2, "*", number3, "=", result2)

# №2

length = int(input("enter first number:"))
width = int(input("enter second number:"))
perimeter = (2 * length) + (2 * width)
print(2, "*", length, "+", 2, "*", width, "=", perimeter)

# №3

diagonal_1 = int(input("enter first number:"))
diagonal_2 = int(input("enter second number:"))
square = 1 / 2 * (diagonal_1 * diagonal_2)
print("1 / 2 * (diagonal_1 * diagonal_2)", "=", square)
