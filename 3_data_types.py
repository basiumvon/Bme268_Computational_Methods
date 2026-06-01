comp=2j
myList=["apple", "banana", "cherry"]
myTuple=("red", "green", "blue")
myRange=range(7) #randge data type is used to represent a sequence of numbers, it is commonly used in for loops to iterate a specific number of times.
myDict={"name":"Buse", "age":24, "city":"ankara"} #Dictionary is a collection of key-value pairs, where each key is unique and maps to a specific value. It is used to store and retrieve data based on keys.
mySet={"apple", "banana", "cherry"} #Set is an unordered collection of unique elements. It is used to store multiple items in a single variable, and it does not allow duplicate values.
myFrozenset=frozenset({"apple", "banana", "cherry"}) #Frozen set is an immutable version of a set, meaning that its elements cannot be changed after it is created. It is used to create a set that cannot be modified, which can be useful in certain situations where you want to ensure that the data remains constant.  
myBool=True
x=None #None is a special data type in Python that represents the absence of a value or a null value. It is often used to indicate that a variable has no value or to signify the end of a function that does not return anything.

import sys
y=12

name=b"python" #bytes data type is used to represent a sequence of bytes, which can be used to store binary data such as images, audio files, or any other type of data that is not text. It is commonly used when working with files or network communication where data needs to be transmitted in a binary format.

nAme=memoryview(bytes(5)) #Memory view is a built-in data type in Python that provides a way to access the memory of an object without copying it. It allows you to manipulate the data in place, which can be more efficient than creating a new object. Memory views are commonly used when working with large data sets or when you need to perform operations on the data without creating unnecessary copies.  
print(comp)
print(myList)
print(myTuple)
print(myRange)
print(myDict)
print(mySet)    
print(myFrozenset)  
print(myBool)
print(x)
print(sys.getsizeof(y))
print(name)
print(nAme) 


y=int(True)
print(y)
print(type(y))


#tuple()
#range()
#dict()
#set()
#frozenset()
#bool()
#None()
#bytes()
#memoryview()
#int()
#str()
#float()
#complex()
#bool()
#list()
# I can use the above functions to convert one data type to another. For example, I can convert a list to a tuple using the tuple() function, or I can convert a string to an integer using the int() function. These functions are useful for manipulating data and performing various operations on different data types.
