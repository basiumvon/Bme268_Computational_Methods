friends = ['Joseph', 'Glenn', 'Sally'] 
friends.sort()
for friend in friends :    
    print('Happy New Year:',  friend) 

for i in range(len(friends)) :    
    friend = friends[i]    
    print('Happy New Year:',  friend)

#valiz=list()
#valiz.append('book')
#valiz.append('99')
#print(valiz)

#ist=[1,2,3,4,5]
#ist.reverse()
#rint(list)


mylist=list()
while True:
    inp=input('enter the num: ')
    if inp=='done':
        break
    val=int(inp)
    mylist.append(val)

average = sum(mylist) / len(mylist) 
print('Average:', average)