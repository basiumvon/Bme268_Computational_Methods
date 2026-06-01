fruit = 'banana' 
index = 0 
while index < len(fruit):     
    letter = fruit[index]    
    print(index, letter)    
    index = index + 1 

fruit = 'banana'       #index = 0            
for letter in fruit:   #while index < len(fruit) : 
    print(letter)          #letter = fruit[index]      #theyr same
                            #print(letter)
                            #index = index +1


#This is a simple loop that loops through each letter in a string and counts the number of times the loop encounters the 'a' character
word='banana'
count=0
for letter in word:
    if letter == 'a':
        count+=1
print(count)

#1.Senaryo: CS2 config (ayar) dosyasından bir satırı okudun ve sadece çözünürlük değerine ihtiyacın var.
# ayar = "resolution: 1280x1024"
#İstenen: Sadece 1280x1024 kısmını ekrana yazdırmak istiyorsun.

ayar= 'resolution: 1280x1024'
index=0
while index<len(ayar):
    letter= ayar[index]
    print(index, letter)
    index+=1      #bu kod sayesinde başlangıç ve bitiş yerlerini biliyoruz ama bunun yerine şöyle de yapabilirdik:

ayar='resolution: 1280x1024'
baslangic=ayar.find('1')
print(baslangic)
bitis=ayar.find('4',baslangic)
print(bitis)    #bu kod da baslangıcı 12 bitisi20 verdi artık slicing e başlayabiliriz.
istenen= ayar[baslangic:bitis+1]
print(istenen)

#Senaryo: Sığınağın telsizine diğer kamptan bir mesaj geldi ama mesaj boşluklar ve büyük/küçük harf karmaşasıyla dolu.
#Veri: sinyal = "   ZomBiLer YaKlaSiYor   "
# İstenen: Bu mesajı bilgisayarın arka arkaya uygulayacağı 3 metot ile tamamen temizle.
# Önce .strip() kullanarak o baştaki ve sondaki gereksiz boşlukları (whitespace) yok et. 
# Sonra .lower() kullanarak mesajın tamamını küçük harfe çevir.
# Son olarak .replace() kullanarak "zombiler" kelimesini "hedefler" kelimesiyle değiştir.
# Temizlenmiş nihai mesajı ekrana yazdır.

msj='   ZomBiLer YaKlaSiYor   '
msj=msj.strip()
msj=msj.lower()
msj=msj.replace('zombiler','hedefler')
print(msj)

#Slayt 30'daki o meşhur e-posta parçasını söküp alma mantığını tam olarak burada uygulayacaksın. Radardan şöyle bir otomatik log kaydı düştü:
#Veri: log = "03:45 AM - Target Spotted at [Sector-B] - Engage"
#İstenen: Sistemine sadece düşmanın bulunduğu yer, yani köşeli parantezlerin içindeki Sector-B verisi lazım.

log="03:45 AM - Target Spotted at [Sector-B] - Engage"
initial=log.find('[')
final=log.find(']')
print(initial)
print(final)
istenen=log[30:38]
print(istenen)

#ex6.5:Take the following Python code that stores a string: str = 'X-DSPAM-Confidence: 0.8475'
#Use find and string slicing to extract the portion of the string after the colon character and then 
# use the float function to convert the extracted string into a floating point number.

str = 'X-DSPAM-Confidence: 0.8475'
ford=str.find(':')
sord=str.find('5')
print(ford,sord)
expected=str[20:]
expected=float(expected)
print(expected)
print(type(expected))
