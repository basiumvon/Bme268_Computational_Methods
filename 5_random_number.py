import random

#random.seed(7) #The seed() function is used to initialize the random number generator. By providing a specific seed value, you can ensure that the sequence of random numbers generated will be the same each time you run the program. This can be useful for testing and debugging purposes, as it allows you to reproduce the same results consistently.

print(random.random())

state=random.getstate() #The getstate() function is used to retrieve the current internal state of the random number generator. This state can be saved and later restored using the setstate() function, allowing you to continue generating random numbers from the same point in the sequence. This can be useful for saving the progress of a random number generation process or for creating reproducible results in certain applications.

print(random.random())

random.setstate(state) #The setstate() function is used to restore the internal state of the random number generator to a previously saved state. By passing the state obtained from the getstate() function, you can continue generating random numbers from the same point in the sequence. This allows you to reproduce results or continue a random number generation process without starting over.

print(random.random())

print(random.random())

print(random.getrandbits(8))

print(random.randrange(1,10)) #The randrange() function is used to generate a random integer within a specified range. It takes two arguments: the start and end of the range. The generated random integer will be greater than or equal to the start value and less than the end value. For example, random.randrange(1, 10) will generate a random integer between 1 and 9 (inclusive of 1 but exclusive of 10). This function is commonly used when you want to generate random numbers within a specific range for various applications such as games, simulations, or data analysis.

print(random.randrange(1,10,4)) #The randrange() function can also take a step argument, which allows you to specify the increment between the numbers in the range. In this case, random.randrange(1, 10, 2) will generate a random integer between 1 and 9 (inclusive of 1 but exclusive of 10) with a step of 2. This means that the generated random integer will be either 1, 3, 5, or 7. The step argument is useful when you want to generate random numbers that follow a specific pattern or when you want to skip certain values in the range.

print(random.randint(1,10)) #The randint() function is used to generate a random integer between a specified range, including both the start and end values. It takes two arguments: the start and end of the range. For example, random.randint(1, 10) will generate a random integer between 1 and 10 (inclusive of both 1 and 10). This function is commonly used when you want to generate random numbers for various applications such as games, simulations, or data analysis where you need a random integer within a specific range.    

myList=["cow", "dog", "horse", "rabbit","lion"]
print(random.choice(myList)) #The choice() function is used to select a random element from a non-empty sequence, such as a list or a tuple. It takes a single argument, which is the sequence from which you want to select an element. For example, random.choice(myList) will randomly select and return one of the elements from the myList. This function is commonly used when you want to randomly select an item from a collection of items for various applications such as games, simulations, or data analysis.

text="I love my Alper Teacher"
print(random.choice(text)) #The choice() function can also be used with strings, as strings are considered sequences of characters. When you use random.choice() with a string, it will randomly select and return one character from the string. For example, random.choice(text) will randomly select and return one character from the text string "I love my Alper Teacher". This can be useful when you want to randomly select a character from a string for various applications such as games, simulations, or data analysis.

mYList=["cow", "dog", "horse", "rabbit"]
print(random.choices(mYList,weights=[5,1,1,1],k=2))

#continue with the shuffle 