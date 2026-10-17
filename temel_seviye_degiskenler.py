"""
Değişken Kavramı: Veriyi saklamak için kullandığımız isimlendirilmiş bir alandır.
    - değişken - bilgiyi tuttuğumuz kutu
    - değişkenleri isimlendirme kuralları:
        - rakamla başlanmaz: 1_var
        - boşluk içermez: berat han
        - özel karakter içermez: önemli_değişken
        - büyük küçük harf duyarlıdır değişken ile Değişken aynı değildir neden çünkü d-D farklı harflerdır ve büyük-küçük harf duyarlılığı vardır

    - Integer: tam sayıları temsil eden değişken tipimiz

    - float: ondalıklı sayıları temsil eder.

    - string: metinsel verileri temsil eder.

    - veri tipi kontrolu ve tip dönüşümleri: bir değişkeni hangi veri tipinde olduğunu öğrenmek ve veri tipleri arasında dönüşüm yapmak
    
    - listeler: birden fazla veriyi tek bir değişken içerisinde saklamamızı sağlar
      - indeksleme ve slicing
      - list metotları

    - tuple: birden fazla veriyi saklayan bir veri yapısıdır, listeye benzer ama önemli bir farkı var tuple değiştirilemez

    - sözlük (dictionary): verileri anahtar-değer (key-value) mantığıyla saklar.

    - set: benzersiz yani unique elemanlardan oluşan bir veri yapısıdır. Aynı elemandan birden fazla kez olamaz.

    - veri yapıları arasınaki farklar: liste, tuple, sözlük, set

"""
# integer
# yaş = özel karakter içerir [ş]
# 1_yas = rakamla başlanmaz
# ogrenci yas = boşluk içermez

yas = 35
ogrenci_sayisi = 55000
sicaklikk = -15

print(yas)
print(35)

# hesaplama
a = 10
b = 5

toplam = a + b # a ve b değerleri toplanmış olur
print(toplam)

çarpma = a * b
print(çarpma)

cikarma = a - b
print(cikarma)

bolme = a/b
print(bolme)

# gerçek hayat örneği: ürün sayısı var ve her bir ürünün birim fiyatı, amaç toplam ürün fiyatı
urun_sayisi = 8 # 8 adet ürün var
birim_fiyat = 10 # birim fiyat 10 tl

toplam = urun_sayisi * birim_fiyat
print(toplam)

# zam uygulaması
# birim_fiyat = 10 # ürünün birim fiyatı 10 tl
# yuzde = int(input("Yüzdeyi yazın: "))
# print(yuzde)
# zamli_fiyat = birim_fiyat + birim_fiyat*yuzde/100
# print(zamli_fiyat)


# float
pi = 3.14
# pi = 3,14 yanlıştır
sicaklik = 35.5
urun_fiyati = 99.99

print(sicaklik)

# matematiksel işlemler
a = 3.5
b = 2.0

print(a + b) # toplam
print(a/b)

# ondalık hassasiyeti
print(0.1 + 0.2)  # 0.30000000000000004 == 0.3

# yuvarlama (round)
sonuc = 0.1 + 0.2
print(sonuc)

sonuc_yuvarlanmis = round(sonuc, 2)
print(sonuc_yuvarlanmis)

# proje: gelen fiyat üzerinden kdv (%20) hesapla 

# fiyat = float(input("Fiyat Girin: "))
# print(fiyat)
# kdvli_fiyat = fiyat + 20*fiyat/100
# print(kdvli_fiyat)

# String
isim = 'berat' # tek tırnak örneği
bölüm = "ybs" # çift tırnak örneği

bilgi = "berat mert değermenci editör veri bilimci"
print(bilgi)

# string birleştirme (concatenation)
isim = "berat mert"
bölüm = "ybs"
bilgi2 = isim + " değermenci " + bölüm + " " + "veri bilimci"
bilgi3 = isim + " değermenci " + bölüm +  " veri bilimci "
print(bilgi2)

# string ve sayı birleştirme
yas = 35 # int
int_to_str = str(yas) # 35 -> "35"
isim = "berat" # string
sonuc = isim + " yaşı " + int_to_str
print(sonuc)

doğum_gunu = 10.01 
int_to_str =str(doğum_gunu)
isim = "berat"
sonuc = isim + " doğum gunu " + int_to_str
print(sonuc)

dogum_yili = 2006
print("berat " + str(dogum_yili) + " yılında dogdu. " )
print(f"berat {dogum_yili} yılında dogdu." ) # f string

accuracy = 95
print(f"karar ağacı accuracy: {accuracy} %")

# string indeksleme
kelime = "python" # string = karakter dizisi
print(kelime[0])
print(kelime[3])

# string metotları
metin = "Python"
metin_kucuk_harf = metin.lower()
print(metin_kucuk_harf)

# uzunluk bulma
metin = "python"
metin_uzunlugu = len(metin)
print(metin_uzunlugu)

# yer değiştirme 
metin = "python"
print(metin.replace("o", "O"))

# veri tipi kontrolu
x = 10
print(type(x)) # <class 'int'>

x = "10"
print(type(x)) # <class 'str'>

# print("25" + 5) # can only concatenate str (not "int") to str

# tip dönüşümleri (casting)
x = "25" # str
print(type(int(x))) # <class 'int'>
print(type(float(x))) # <class 'float'>

x = 35
print(type(str(x))) # <class 'str'>

# sayi = int(input("Bir sayı girin: ")) # input fonk çıktısı ne olabilir int? str?
# print(sayi) # 45 int? str?
# print(type(sayi)) # <class 'str'>

# print(int("abc")) # ValueError: invalid literal for int() with base 10: 'abc'

# listeler
# liste tanımlaması köşeli paranztez ile gerçekleşir
sayilar = [1, 2, 3, 4, 5, 6] # integer listesi
isimler = ["berat", "mert", "degermenci", "ybs"] # string listesi
karisik = ["berat", 1, "mert", "ybs", 55, 61.1] # farklı veri tiplerini aynı anda tutabilir

print(karisik) # ['berat', 1, 'mert', 'ybs', 55, 61.1]

# liste indeksleme: listelerde indeks 0'dan başlar
meyveler = ["elma", "muz", "kivi"]

print(meyveler[0]) # elma
print(meyveler[2]) # kivi
print(meyveler[-1]) # kivi
print(meyveler[-2]) # muz

# liste uzunluğu
print(len(meyveler)) # 3

# listeler slicing
sayilar = [10, 20, 30, 40, 50, 60]
print(sayilar[1:4]) # 20, 30, 40  [a:b] a dahil, b dahil değil
print(sayilar[0:3]) # ilk 3 eleman 10, 20, 30
print(sayilar[:3]) # ilk 3 eleman 10, 20, 30   0 yazmayabilir
print(sayilar[2:]) # 30 dan sonrası
print(sayilar[:4]) # 50 den önce
print(sayilar[2:5]) # [30, 40, 50]
print(sayilar[4:5]) # 50
print(sayilar[0:]) # [10, 20, 30, 40, 50, 60]

# listeye eleman eklemek
sayilar = [1, 2, 3]
sayilar.append(4) # eleman ekleme
print(sayilar) # [1, 2, 3, 4]

sayilar.insert(1, 100)
print(sayilar) # [1, 100, 2, 3, 4]

sayilar.remove(100) # eleman silme
print(sayilar)

sayilar.pop() # en son indekste bulunan değer çıkartılır
print(sayilar) # [1, 2, 3]

sayilar.pop(0) # belirli bir indeks silinir
print(sayilar)

sayilar[0] = 999 # belirli bir indeksteki değeri başka bir değerle değişir
print(sayilar)

# UYGULAMA
# liste = [1, 7, 10, 48, 61, 88, 102, 199]
# print(liste[2:6]) # [10, 48, 61, 88]
# print(liste[:7]) # [1, 7, 10, 48, 61, 88, 102]
# print(liste[0:]) # [1, 7, 10, 48, 61, 88, 102, 199]

# liste.append(50) # eleman ekleme
# print(liste) # [1, 7, 10, 48, 61, 88, 102, 199, 50]

# liste.insert(5, 70) # belirli bir yere sayı ekleme
# print(liste) # [1, 7, 10, 48, 61, 70, 88, 102, 199]

# liste.remove(88) # eleman silme
# print(liste) # [1, 7, 10, 48, 61, 70, 102, 199]

# liste.pop(7)  # belirli bir eleman silinir
# print(liste)  # [1, 7, 10, 48, 61, 70, 102, 50]
 
# liste.pop()   # liste sonundaki eleman silinir
# print(liste)  # [1, 7, 10, 48, 61, 70, 102]

# liste[5] = 100
# print(liste)

# tuple -> ()
koordinat = (10, 20)
renkler = ("kırmızı", "mavi", "yesil")

# liste vs tuple
liste = [1, 2, 3]
liste[0] = 99
print(liste)  # [99, 2, 3]

# tup = (1, 2, 3)
# tup[0] = 99
# print(tup) # TypeError: 'tuple' object does not support item assignment

# indeksleme 
t = (10, 20, 30)
print(t[1]) # 20
print(t[-1]) # 30

# slicing
t = (10, 20, 30, 40)
print(t[1:3])  # (20, 30)

# tek elemanlı tuple
x = (5) # x = 5
print(type(x)) # tuple? int? cevap -> <class 'int'>

x = (5,)
print(type(x)) # <class 'tuple'>

# tuple unpacking
koordinat = (10, 20)
x, y = koordinat
print(x) # 10
print(y) # 20

# tuple metotları
t = (20, 20, 30, 40)

print(t.count(20)) # 2  20 den kaç tane var
print(t.index(30)) # 2  indeks sırası

# t = (35, 35, 43, 44, 55, 55, 62, 43, 12, 12, 12, 35, 55, 62, 43, 44, 1, 2, 2, 3, 43, 35)
# print(t.count(35)) # 4
# print(t.count(55)) # 3
# print(t.index(43)) # 2

# x = (10,)
# print(type(x)) # <class 'tuple'>

# sözlük (dicitonary) 
ogrenci = { # issm = anahtar, berat = key değeri -> (anahtar = değer)
    "isim": "berat",
    "yas": 25,
    "bolum": "ybs"
}
print(ogrenci)

# dictionarye erişim
print(ogrenci["isim"]) # berat
print(ogrenci["yas"])  # 25

# dictionary yeni değer ekleme
ogrenci["not"] = 85
print(ogrenci) # {'isim': 'berat', 'yas': 25, 'bolum': 'ybs', 'not': 85}

# dictionary değer güncelleme
ogrenci["yas"] = 26
print(ogrenci) # {'isim': 'berat', 'yas': 26, 'bolum': 'ybs', 'not': 85}

# dictionary eleman silme
del ogrenci["bolum"]
print(ogrenci) # {'isim': 'berat', 'yas': 26, 'not': 85}

# anahtarları ve değerleri al
print(ogrenci.keys()) # anahtarlar
print(ogrenci.values()) # değerler
print(ogrenci.items()) # anahtar - değer

"""
dict_keys(['isim', 'yas', 'not'])
dict_values(['berat', 26, 85])
dict_items([('isim', 'berat'), ('yas', 26), ('not', 85)])
"""

# set
sayilar = {1, 2, 3, 4}
print(sayilar) # {1, 2, 3, 4}

# set tekrar eden elemanlar
sayilar = {1, 2, 2, 3, 3, 3}
print(sayilar) # {1, 2, 3}

# set özellikleri: setler sırasızdır yani indeksi yoktur
# print(sayilar[2]) TypeError: 'set' object is not subscriptable

# listeyi sete çevirme
liste = [1, 2, 2, 3, 4, 4]
benzersiz = set(liste)
print(benzersiz) # {1, 2, 3, 4}

# sete eleman ekleme
sayilar.add(5)
print(sayilar) # {1, 2, 3, 5}

# set eleman silme
sayilar.remove(2)
print(sayilar) # {1, 3, 5}

# set işlemleri
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b)) # birleşim {1, 2, 3, 4, 5}

print(a.intersection(b)) # kesişim  {3}

print(a.difference(b)) # fark {1, 2}

"""
liste:
     - Sıralıdır, değiştirilebilir, tekrar eden elemanlara izin verir
     - liste = [1, 2, 3]
     - kullanım: eleman sırası önemliyse, veri güncellenecekse
     - numpy array in temelini oluşturmaktadır

Tuple:
     - sıralıdır, değiştirilemez, tekrar eden elemanlara izin verir
     - tuple = (1, 2, 3, 4)
     - kullanım: veri sabit kalacaksa, güvenli yapı gerekiyorsa

dictionary:
     - anahtar-değer (key-value pair)
     - anahtarlar benzersizdir
     - değerler tekrar edebilir
     - değiştirilebilir
     - öğrenci = {"isim":"berat","yas": 20}
     - anlamlı veri saklamak, etiketli veri tutmak
     - pandas dataframe temelini oluşturur

Set:
    - sırasızdır, tekrar eden elemanları kabul etmez, değiştirilebilir
    - set = (1, 2, 3, 4)
    - kullanım: tekrar eden değerleri temizlemek için kullanılır, küme işlemleri yapmak için kullanılır

"""