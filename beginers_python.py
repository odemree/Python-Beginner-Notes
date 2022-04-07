''' Print ve Format Fonksiyonu,Yorum Satırları '''
print("salamu alaykum")
print("salamualaykum")
print("hello world!")
print("tırnak içine yazılan sayı (1,2,3,4,5 vs.)'de metinsel olarak algılanır.")
print("salamualaykum","salamu","alaykum","salamu alaykum","salamu"  "alaykum","14 15 16","14,15,16",14,15,16)
print("salamu\nalaykum\nbaba")
print(" salamu\n alaykum\n baba")
print("11 03 2006")
print("11,03,2006")
print("11","03","2006")
print("11""03""2006")
print("11","03","2006",sep = "/")
print("11""/""03""/""2006")
print("11/03/2006")
print("{} + {} = {}".format (2,3,5))
print("{} + {} = {}".format (2,3,2+3))
print("{} + {} = {}" .format (2,3,5))
print("{} + {} = {}"  .format (2,3,5))
print("{} + {} = {}".format ("2","3","5"))
print("{} + {} = {}".format ("2","3",3+2))
# bu tag işareti kod satırı yazarken not almamızı sağlar kod olarak okunmaz, çalıştırılmaz veya kullanılmaz. YORUM SATIRI OLARAK ADLANDIRILIR.
'''üç tırnak fonksiyonu kod satırı yazarken not almamızı sağlar kod olarak okunmaz, çalıştırılmaz veya kullanılmaz. YORUM SATIRI OLARAK ADLANDIRILIR. '''
'''üç tırnak fonksiyonu kod satırı yazarken not 
almamızı sağlar kod olarak okunmaz, 
çalıştırılmaz veya kullanılmaz. YORUM SATIRI OLARAK ADLANDIRILIR. '''
'''
üç tırnak fonksiyonu kod satırı yazarken not 
almamızı sağlar kod olarak okunmaz, 
çalıştırılmaz veya kullanılmaz. YORUM SATIRI OLARAK ADLANDIRILIR.
'''
print("abe")
print(155)


''' Değişkenler,Veri Tipleri '''
a = 3 #Numerik (sayısal) veri tipleri → int → integer (tamsayı)
b = 5.5 #Numerik (sayısal) veri tipleri → float (ondalık sayı)
c = "Pyhton" #String (metin) veri tipleri → str
d = "Pyhton55" #String (metin) veri tipleri → str
e = "55" #String (metin) veri tipleri → str
f = [1,2,3,4,5,"Python"] #Sequence (sıralama) veri tipleri → list
g = (1,2,3,5,"Python") #Sequence (sıralama) veri tipleri → tuple
h = {"Elma":5 ,"Armut":10,"Kiraz":20} #Mapping (haritalama) veri tipleri → dict (sözlük)
i = True  #Boolean veri tipleri → bool
j = False #Boolean veri tipleri → bool
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j)) #type fonksiyonu kodun hangi veriye ait olduğunu gösterir.
print(a,b,c,d,e,f,g,h,i,j)
print("a,b,c,d,e,f,g,h,i,j")
print("a","b","c","d","e","f","g","h","i","j")
print("a b c d e f g h i j")


''' Matematik Operatörleri '''
print(2 + 8)
print(5 * 2)
print(8 - 4)
print(8 / 4)
print(8 // 4)
print(10 / 4)
print(10 // 4) #çift eğik çizgi tamsayı bölmesi yapmayı sağlar.
print(10 % 4) #kalanı bulmayı sağlar.
a = 5
b = 10
print(a * 10 / 2 + b)
print(a * 10 / (2 + b))
a = "Python"
b = "Programlama"
c = "Dili"
d = a + b + c
print(d)
a = "Python "
b = "Programlama "
c = "Dili"
d = a + b + c
print(d)
a = "Python"
b = " Programlama"
c = " Dili"
d = a + b + c
print(d)
a = "Python"
b = " Programlama "
c = "Dili"
d = a + b + c
print(d)
a = "Python"
print(a * 5)
a = "Python "
print(a * 5)
print("* " * 1)
print("* " * 2)
print("* " * 3)
print("* " * 4)
print("* " * 5)
print("* " * 6)
print("* " * 7)

print("       *" * 1)
print("      *" * 2)
print("     *" * 3)
print("    *" * 4)
print("   *"  * 5)
print("  *" * 6)
print("*" * 7)


''' String ve Listelerin Indekslenmesi '''
a = "Python"
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(len(a))
print(a[len(a)-3])
print(a[0:4])
print(a[0:])
print(a[3:])
print(a[:3])
print(a[:])
print(a[2:2])  #sonuç ekranında boş satır bırakmak için kullanılabilir.
print(a[::2])
print(a[0:5:2])
b = [1,2,3,4,5,6,7]
print(b[0])
print(b[1])
print(b[2])
print(b[3])
print(b[4])
print(b[5])
print(b[6])
print(len(b))
print(b[len(b)-3])
print(b[0:4])
print(b[0:])
print(b[2:])
print(b[:3])
print(b[:])
print(b[2:2])
print(b[::2])
print(b[0:6:2])

a = {"Elma":5,"Armut":6,"Kiraz":7,"Karpuz":8}
print(a["Elma"])
print(a["Karpuz"])
print(a["Kiraz"])
print(a["Armut"])


'''  Input Alma '''
'''yas = input("Yaşınızı Giriniz ")
print("Yaşınız",yas)
a = input("a:")
b = input("b:")
c =input("c:")
print("Toplam",a + b + c) #hatalı bir durum çünkü değerleri metinsel olarak algıladı bizim bu değerleri integar'a dönüştürmemiz gerekiyor. bu yüzden başına int ifadesi ekliyoruz.
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
print("Toplam",a + b + c)''' #3 tırnak içine aldım çünkü çalışma devamında sorular tekrarlamasın diye. Kullanılırken kaldırılabilir.

'''dogum = int(input("Doğum Yılınız "))
print(("Yaşınız"),(2021 - dogum)) kendi başıma yazdığım ilk kod. bir yaş hesaplayıcı :) '''


''' Koşullu Durumlar (if - elif - else) '''
'''yas = int(input("Yaşınız Girin: "))
if yas < 18:
    print("İçeriye Giremezsin Evlat!")
else: print("Hoşgeldiniz Buyrun...")'''

'''islem = int(input("İşlem Giriniz "))
if islem == 1:
    print("İşlem 1 Başarıyla Seçildi")
elif islem == 2:
    print("İşlem 1 Başarıyla Seçildi")
elif islem == 3:
    print("İşlem 3 Başarıyla Seçildi")
else:
    print("Geçersiz İşlem Seçimi")'''

''' Mantıksal Operatörler '''
a = 10
b = 20
c = 30
if a == 10 and b == 20 and c == 30:
    print("Hepsi Doğru Kabul Edildiniz.")
else:
    print("Yanlış Cevap Var. Kontrol Ediniz")

a = 10
b = 20
c = 30
if a == 10 and b == 15 and c == 30:
    print("Hepsi Doğru Kabul Edildiniz.")
else:
    print("Yanlış Cevap Var. Kontrol Ediniz.")

a = 10
b = 20
c = 30
if a == 11 or b == 15 or c == 38:
    print("Hepsi Doğru Kabul Edildiniz.")
else:
    print("Yanlış Cevap Var. Kontrol Ediniz.")

if (not(4 > 2)):
    print("Evet")

if (not(4 > 4)):
    print("Yanlış")


''' While Döngüsü '''
a = 0
while a < 15:
    print("a değeri: ",a)
    a = a + 1

a = "Python"
print(a[2:2])

a = 0
while a < 15:
    print("a değeri: ",a)
    a = a + 2


''' Break ve Continue '''
'''i = 0
while (i < 10):
    if i == 5:
        break
    print("i' nin değeri: ",i)
    i += 1'''

i = 0
while (i < 10):
    if i == 3 or i == 5:
        i += 1
        continue
    print("i değeri: ",i)
    i += 1


'''   For Döngüsü ve Range Fonksiyonu '''
Rakamlar = [1,2,3,4,5,6,7,8,9,0]
for rakam in Rakamlar:
    print(rakam)

Yazı = ["Python Kodları"]
for karakter in Yazı:
    print(karakter)

Yazı = "Python Kodları"
for karakter in Yazı:
    print(karakter)

a = "Python"
print(a[2:2])

for sayı in range(0,100):
    print(sayı)
a = "Python"
print(a[2:2])
for sayı in range(95,101):
    print(sayı)
a = "Python"
print(a[2:2])
for sayı in range(0,105,5):
    print(sayı)


''' Fonksiyonlar '''
def selamla():
    print("Merhaba")
    print("Nasılsınız?")
selamla()

def selamla():
    print("Merhaba")
    print("Nasılsınız?")
selamla()
selamla()
selamla()
selamla()
selamla()
selamla()

def selamla(isim = ""):
    print("Merhaba",isim)
selamla("Murat")
selamla("Ayşe")
selamla("Selim")
selamla("Fatma")
selamla()

def toplama(a,b,c):
    print("Toplam:",a+b+c)
toplama(2056,8156,1087)

def toplamaveeşitleme(a,b,c):
    print("Toplam Sayı:",a-b-c)
toplamaveeşitleme(20,10,5)


''' Listelerin ve Stringlerin Bazı Metodları '''
liste = [1,2,3,4,5,6]
a = "Python Çalışmam"
print(len(liste))
print(len(a))
print(a.startswith("P"))
print(a.startswith("p"))
print(a.startswith("H"))
print(a.startswith("Py"))
print(a.startswith("PY"))
print(a.startswith("Python Çalışmam"))
print(a.endswith("m"))
print(a.endswith("mam"))
print(a.endswith("Çalışmam"))
print(a.endswith("Python Çalışmam"))
a = a.replace("a","o")
print(a)
a = a.replace("m","n")
print(a)
liste =[1,2,3,4,5,6]
liste.append("Python mu?")
print(liste)
liste.pop()
print(liste)
liste.pop(0)
print(liste)
liste.pop(1)
print(liste)
liste.pop(2)
print(liste)
liste.pop(3)
print(liste)
liste.pop(4)
print(liste)
liste.pop(5)
print(liste)