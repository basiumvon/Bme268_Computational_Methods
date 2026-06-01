#1.Senaryo: Sığınak Jeneratörü Yakıt Tüketimi. Elimizde jeneratörün son 5 günde harcadığı yakıt miktarlarını (litre cinsinden) tutan bir liste var
# yakitlar = [45, 20, 60, 15, 30]. Bir for döngüsü kur.
#Döngüden önce yaratacağın sepet (sum) ve sayaç (count) değişkenlerini kullanarak toplam harcanan yakıtı ve günlük ortalama yakıt tüketimini hesapla.
#Döngü bittikten sonra ekrana toplamı ve ortalamayı yazdır.

sum=0
count=0

for fuel in [45, 20, 60, 15, 30]:
    sum+=fuel
    count+=1
    average_consuption=sum/count
print('Total amount of fuel consumed in one day: ',sum,' Liters.')
print('The average consuptionis: ',average_consuption,' Liters.')

#2.Senaryo: Yakın Mesafe Zombi Radarı
#Sığınağın radarı etraftaki hareketliliklerin metre cinsinden uzaklıklarını şu listeye kaydetti:
#mesafeler = [120, 45, 78, 12, 5, 300, 49]
#Bir for döngüsü ile bu listeyi tara.0
#Sadece sığınağa 50 metreden daha yakın olan tehlikeleri (50'den küçük sayıları) ekrana "DİKKAT! Tehlike yaklaşıyor: [mesafe] metre" şeklinde yazdır.
#50 metreden uzak olanları tamamen es geç.

i=0
for distance in [120, 45, 78, 12, 5, 300, 49]:
    i+=1
    if distance<50:
        print('Caution! zombie',i,' is getting closer!:', distance,'meter!')
    else:
        continue

#3.Senaryo: En Yüksek Radyasyon Bölgesi. Keşif ekibi dışarıdaki 6 farklı bölgeden radyasyon seviyeleri ölçtü:
#radyasyonlar = [15, 8, 42, 3, 99, 27]. En yüksek radyasyon seviyesini bul.

The_larg=0
for radiation in [15, 8, 42, 3, 99, 27]:
    if The_larg<radiation:
        The_larg=radiation
    else:
        continue    
print('The highest radiation region is ',The_larg,'.')

#4.Senaryo: En Kritik Erzak Stoğu
#Sığınaktaki 5 farklı deponun erzak dayanma süreleri (gün cinsinden) listede verilmiş:
#stok_gunleri = [150, 45, 12, 300, 90]. Döngü bittikten sonra "En acil erzak takviyesi gereken depo ömrü: 12 gün" yazdır. (Yine min() fonksiyonu kullanmak yasak).

smallest=None
for days in [150, 45, 12, 300, 90]:
    if smallest is None:
        smallest=days
    elif days<smallest: # banttan gelen sayı elimdekinden küçük mü?
        smallest=days #küçükse at cebe abla

print('Storage life requiring the most urgent resupply: ',smallest,' days.')

 