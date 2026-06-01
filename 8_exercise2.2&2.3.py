# Exercise 2.2
name=input('Enter your name: ')
print( 'Hello ',name) #print('Hello ' + name) also works, but the comma adds a space between the two strings automatically, while the plus operator does not.

# Exercise 2.3
hour=input('Enter the number of hours: ')
rate=input('Enter the hourly rate: ')
pay=float(hour)*float(rate) #if we sont convert the input to float, it will be treated as a string and the multiplication will result in string replication instead of numerical multiplication.
print('Pay: ',pay)
