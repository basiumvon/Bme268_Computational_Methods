#Görev: Kullanıcıdan bir sayı (veya metin) al. while döngüsü kullanarak bu girdiyi tersten yazdıran bir kod yaz.
#Şart: İndeksleme veya hazır reverse() fonksiyonu kullanma. Sadece döngü ve matematiksel işlemler veya string ekleme yöntemiyle yap.
def tersini_al(metin):
    tersi=""
    index=len(metin)-1

    while index>=0:
        tersi=tersi+metin[index]
        index=index-1
    return tersi
sayi=input('Enter number:')
print(tersini_al(sayi))

#Problem: Write a function that calculates the square of each number in a given list. [
# Define a function named square_elements(num_list).
# The function must return a new list containing the squares of the numbers.
# In the main program, iterate through the result of this function using a for loop and print each squared value.

def sayilari_topla ():
    list1=[]
    while True:
        eleman=input('enter a num: ')
        if eleman=='done':
            break
        sayi=float(eleman)
        list1.append(sayi)
    return list1

def kare_al(liste):
    kareler=[]
    for x in liste:
        x=x*x
        kareler.append(x)
    return kareler

mylist=sayilari_topla()
sonuc=kare_al(mylist)

print(sonuc)