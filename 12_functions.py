# Why we use return function in python?
#1- It allows us to recall the function multiple times without having to rewrite the code.
#2- try/except block can be used to handle exceptions and errors that may occur during the execution of a function. By using return statements, we can provide feedback on the success or failure of the function, allowing us to handle errors gracefully and prevent crashes in our program.

 

midterm=input('Enter your midterm grade: ')
final=input('Enter your final grade: ')

def ortalama(midterm,final):

    try:
        fixmt=float(midterm)
        fixfnl=float(final)
        ort=(fixmt*0.4)+(fixfnl*0.6)
        return ort
    except:
        print('Please enter invalid number.')
        return -1


grade=ortalama(midterm,final)

if grade==-1:
   print('')
elif grade>=90:
 print("Your grade is ",grade, " AA")
elif grade>=80:
 print("Your grade is ",grade, " BA")
elif grade>=70:
 print("Your grade is ",grade, " BB")
elif grade>=60:
 print("Your grade is ",grade, " CB")
elif grade>=50:
 print("Your grade is ",grade, " CC")
elif grade<50:
 print("Your grade is ",grade," You are failed")

    



        
def analiz(grade):
    if grade ==-1:
        return 'GEÇERSİZ!'
    elif grade>= 50:
        return 'Başarili!'
    else:
        return 'Başarisiz'
            
print(analiz (grade ))


#3- To shutdown the program when we want to stop the execution of the function and return a value to the caller. This can be useful in situations where we want to exit a function early or return a specific result based on certain conditions. By using return statements, we can control the flow of our program and ensure that it behaves as expected.

