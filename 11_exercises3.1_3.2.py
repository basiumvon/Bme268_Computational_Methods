#3.1: rewrite your pay computation to give yhe employee 1.5 times the hourly rate for hours worked above 40 hours

hrs=input("enter hours worked:")
rate=input('enter your hourly rate:')
fhrs=float(hrs)
frate=float(rate)

if fhrs>40:
    reg=frate*40
    otp=(fhrs-40.0)*frate*1.5
    pay=reg+otp
    print("overtime and your pay is :" , pay)
   
else:
    pay=fhrs*frate
    print("Regular and your pay is :", pay)



    

#3.2: rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a messsage and exiting the program. 

hrs=input("enter hours worked:")
rate=input('enter your hourly rate:')

try:
    fhrs=float(hrs)
    frate=float(rate)
except:
    print("Error, please enter numeric input")
    quit()
if fhrs>40:
    reg=frate*40
    otp=(fhrs-40.0)*frate*1.5
    pay=reg+otp
    print("overtime and your pay is :" , pay)
else:
        pay=fhrs*frate
        print("Regular and your pay is :", pay)