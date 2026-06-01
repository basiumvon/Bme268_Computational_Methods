str='senin en güzel yerin kahverengi gözlerin'
stuff=str.split()
print(stuff)
print(len(stuff))

str2='canım;çoksıkıldı;yazılımdan;nefret;ediom'
stuff2=str2.split(';')
print(stuff2)
print(len(stuff2))

fhand=open('ex.7.1.txt','r')
for line in fhand:
    if not line.startswith('FROM'):
        continue
    text=line.split()
    print(text)
    textr=text[1]
    print(textr)
    pieces=textr.split('@')
    print(pieces)
    pieces=pieces[1]
    print(pieces)

    a=[1,2,3]
    b=a
    a.append(4)
    print(b)