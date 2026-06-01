# \n alt satır boşluk bırakır
# \t tab boşluk bırakır
# \r imleci satır başına getirir 
#19E4 matematiksel bir gösterimdir E 10 üzerini temsil eder, yani 19E4 ifadesi 19 x 10^4 anlamına gelir ve sonucu 1900000 olur. 

# Circle Area and Circumference Calculator
#Circle Area = π * r^2
#Circle Circumference = 2 * π * r

pi=3.14159
r=float(input("Enter the radius"))

circleArea=float(pi*r*r)
circleCircumference=float(2*pi*r)

print("Area:",circleArea)
print("Circumference:",circleCircumference)