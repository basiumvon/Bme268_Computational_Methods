#Exercise 1: Write a program which repeatedly reads integers until the user enters “done”. Once “done” is entered, 
# print out the total, count, and average of the integers. If the user enters anything other than an integer, 
# detect their mistake using try and except and print an error message and skip to the next integers.
total=0
count=0
while (True):
    girdi=input('enter a number: ')
    if girdi!='done':
        try:
            girdi=int(girdi)
        except:
            print('Enter invalid')
        total+=girdi
        count+=1
        avg=total/count
    if girdi=='done':
        break

print('total: ',total )
print('avg: ',avg)