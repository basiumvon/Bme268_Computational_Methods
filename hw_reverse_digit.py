number = int(input("Enter an integer: "))
reversed_number = 0
temp_number = number

while temp_number > 0:
    last_digit = temp_number % 10
    reversed_number = (reversed_number * 10) + last_digit
    temp_number //= 10

print("The reversed number is:", reversed_number)