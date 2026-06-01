
astr='hello'
try:
    istr=int(astr)
except:
    istr=-1

print('The value of istr is:',istr)


number=input("Enter a positive number: ")
try:
    var=int(number)
except:
    var=-1

if var>0:
    print('Nice work')

else:    print('Not a number')