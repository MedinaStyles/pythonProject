# Task1
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))
result = (number1 * 10 + number2) * 10 + number3
print(result)


# Task2
number = int(input("enter number: "))
number1 = number / 1000
number2 = (number1 - int(number1)) * 10
number3 = (number2 - int(number2)) * 10
number4 = (number3 - int(number3)) * 10
result = int(number1) * int(number2) * int(number3) * int(number4)
print(int(number1), "*", int(number2), "*", int(number3), "*", int(number4), "=", result)

# Task2 (another varint)
number = int(input("enter number: "))
number1 = number / 1000
number2 = ((number1 - int(number1)) * 100) // 10
number3 = ((number1 - int(number1)) * 1000) // 10 - number2 * 10
number4 = ((number1 - int(number1)) * 10000) // 10 - number2 * 100 - number3 * 10
result = int(number1) * int(number2) * int(number3) * int(number4)
print(int(number1), "*", int(number2), "*", int(number3), "*", int(number4), "=", int(result))
