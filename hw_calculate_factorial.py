number = int(input("Enter a number to calculate its factorial: "))
factorial_result = 1

for i in range(1, number + 1):
    factorial_result *= i

print("The factorial of", number, "is", factorial_result)