#rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).

def computepay (hours,rate):
    if hours >40:
        reg= rate*hours
        otp=(hours-40) * (rate*0.5)
        pay=reg + otp
    else:
        pay=hours*rate
    return pay

sh=input('enter hours: ')
sr=input('Enter rate: ')
fh=float(sh)
fr=float(sr)

xp= computepay(fh,fr)

print('Pay: ',xp)