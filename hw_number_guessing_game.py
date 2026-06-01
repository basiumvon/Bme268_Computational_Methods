import random

target_number = random.randint(1, 100)
user_guess = 0

print("I've picked a number between 1 and 100.")
while user_guess != target_number:
    user_guess = int(input("Enter your guess: "))
    if user_guess < target_number:
        print("Too low!")
    elif user_guess > target_number:
        print("Too high!")
    else:
        print("Correct! You win!")
        