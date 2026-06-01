#Variable
x=7
y= "python"
z= 5.5
v= 'awesome'

print(x)
print(y)
print (x*z)
print(v)

a= str(3)
b= int(3)
c= float(3)
print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


#VARIABLE NAMES 
_name="Buse"
name="Bme"
# 2name="abdullrahman" #olmaz
print(_name)
print(name) 

j,k,l=6,7,8

g=h=f="red"
print(g)
print(h)
print(f)

#Variable unpacking

fruits=["apple","banana","cherry"]
t,m,n=fruits
print(t)
print(m)
print(n)


#Global and local Variables

text="marvellous"

def myFunction():
    text="fantastic"
    print("Python is "+text)

myFunction()
print("Python is "+text)

#if you want to create a global variable inside a function, you can use the global keyword.

def myFunction2():
    global text
    text="awesome"
    
myFunction2()
print("Python is "+text)



# input() function is used to take input from the user. It always returns a string. So you can convert it to the desired data type using int(), float(), etc.   

floor=input('Enter the floor number: ')
us_floor=int(floor)+1
print("The floor number in US is: ", us_floor)