# 1. Adım: Dosyayı 'okuma' modunda aç
fhand = open('siir.txt', 'r') 

# 2. Adım: Her satırı tek tek oku ve bas
for satir in fhand:
    # Her satırın sonunda zaten bir \n var, print de bir tane ekliyor. 
    # O yüzden fazladan boşlukları temizleyelim.
   temsatir=satir.rstrip()
   print(temsatir)

# 3. Adım: Dosyayı kapat (Dosya kolunu serbest bırak)
fhand.close()

fhand =open('siir.txt','r')
print("--- 'Ağlasam' geçen satırlar ---")
for satir in fhand:
   satir=satir.rstrip()
   if 'AÄŸlasam' in satir:
      print(satir)
fhand.close()

fhand = open('siir.txt', 'r')
tum_siir = fhand.read() # Tüm dosyayı tek bir string değişkenine kopyala 

print("Dosyanın toplam karakter sayısı:", len(tum_siir))
print("Şiirin ilk 20 karakteri:", tum_siir[:20]) # Slice (Dilimleme) kullandık 

fhand.close()

fout=open('deneme.txt','w')
line1='Bu benim pythondan acip yazdigim ilk dosyam.\n'
fout.write(line1)
fout.close()
#Şimdi öğrendiğin bu yeni "yazma" ve "kapama" yeteneklerini kullanarak, senin anlatamiyorum.txt dosyanı alıp, 
#içindeki her şeyi büyük harfe çeviren ve başka bir dosyaya kaydeden şu programı yazalım

fhand=open('siir.txt','r')
fout=open('deneme.txt','w')

for satir in fhand:
   fout.write(satir.upper())

fhand.close()
fout.close()
