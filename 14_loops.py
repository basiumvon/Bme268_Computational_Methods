#1.Sığnağın kapısına bir şifre paneli yapılacak. Sistem kulllanıcıdan sürekli şifre isteyecek.

while(True):
    password=input('To open the gate please enter the password, if you wanna leave please enter \'exit\': ') 
   
    if password=='1234':
        print('WELLCOME! The Gate is Openning')
        break
    elif password=='exit':
        print('System is shutting down!')
        break
    else:
        print('Wrong password TRY AGAIN!')

#2.Elinde sığnağa gelen erzakların kalori değerleri var. Ancak (-) değerde olanlar zehirli/bozuk erzakları temsil ediyor. temiz erzak kalorilerini listele. 
#Supplies=[150, 200, -50, 300, -100, 400]
i=1
total_calori=0
for supply in [150, 200, -50, 300, -100, 400]:
    if supply<0:
        continue
    elif supply>0:
        
        print('Safe suplly',i, ': [',supply,'kcal].')
        i+=1
        total_calori+=supply
print('Total Safe Calori: ', total_calori)

#0dan 5 e kadar 5 dahil bir while döngüsü kur. sayı 3 e eşit olduğunda es geç.
i=-1
while i<5:
    i+=1
    if i==3:
        continue
    print(i)
print ('Finish')
