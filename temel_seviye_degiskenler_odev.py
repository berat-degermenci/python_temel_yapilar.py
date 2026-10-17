"""
soru 1
bir değişken tanımlayalım: ad = "berat", yas = 25, ortalama = 3.45
bu degişkenlerin tiplerini type ile yazdıralım.
"""

ad = "berat"
yas = 25
ortalama = 3.45

print(type(ad)) # <class 'str'>
print(type(yas)) # <class 'int'>
print(type(ortalama)) # <class 'float'>

"""
soru 2
kullanıcıdan yaş bilgisi input() ile alalım
bu yasın tipini ekrana basalım ve 5 yıl ekleyip sonucu yazdıralım
not: input() her zaman string döndürür, int'e çevirmeyi unutmayalım
"""

# yas_str = input("yaşı girin: ")
# print("gelen veri tipi", type(yas_str))

# yas_int = int(yas_str)
# print("5 yıl sonraki yas:", yas_int + 5)

"""
soru 3
bir ürün fiyatı (float) alalım. %18 kdv hesaplayalım
toplam fiyatı 2 basamak olacak şekilde hesaplayalım
"""

# fiyat = float(input("fiyat girin:"))
# kdv = fiyat * 0.18
# toplam = fiyat + kdv
# print("KDV:", round(kdv, 2))
# print("Toplam:", round(toplam,2))

"""
soru 4
bir liste oluşturalım sayilar = [10, 20, 30, 40, 50]
-ilk elemanı yazdır
- son elemanı yazdır
- 2. indeksten sona kadar olan parçayı yazdıralım
- listeye 60 ekleyelim
- listedeki 20 değerini silelim
"""

sayilar = [10, 20, 30, 40, 50]

print(sayilar[0])
print(sayilar[-1])
print(sayilar[2:])
sayilar.append(60)
print(sayilar)
sayilar.remove(20)
print(sayilar)

"""
soru 5
bir tuple oluştur: koordinat = (12, 34)
tuple içindeki değerleri unpacking ile x ve y değişkenlerine alalım
x ve y yi yazdıralım
tuple ın değiştirilmediğini göstermek için yorum satırıyla örnek verelim
"""

koordinat = (12, 34)
x, y = koordinat
print("x:", x)
print("y:",y)

# koordinat[0] = 99 TypeError: 'tuple' object does not support item assignment
# tuple değiştirelemez


"""
soru 6
bir sözlük oluştur
ogrenci = {"isim": "Berat", "yas": 22, "bolum": "yazılım"}
ogrencinin ismini yazdıralım
"not" anahtarı ile 90 ekleyelim
"yas" degerini 23 yaparak güncelleyelim
tüm anahtarları ve değerleri yazdıralım
"""

ogrenci = {"isim": "Berat", "yas": 22, "bolum": "yazılım"}

print(ogrenci["isim"]) # Berat

ogrenci["not"] = 90
print(ogrenci) # {'isim': 'Berat', 'yas': 22, 'bolum': 'yazılım', 'not': 90}

ogrenci["yas"] = 23
print(ogrenci) # {'isim': 'Berat', 'yas': 23, 'bolum': 'yazılım', 'not': 90}

print(ogrenci.items()) # dict_items([('isim', 'Berat'), ('yas', 23), ('bolum', 'yazılım'), ('not', 90)])

print(ogrenci.keys()) # dict_keys(['isim', 'yas', 'bolum', 'not'])

print(ogrenci.values()) # dict_values(['Berat', 23, 'yazılım', 90])

"""
soru 7
set oluştur ve tekrar edenleri temizle
liste = ["Ali", "Ayşe", "Ali", "Mehmet", "Ayşe"]
listeyi sete çevirip benzersiz isimleri yazdıralım
benzersiz isim sayısını yazdıralım
"""

liste = ["Ali", "Ayşe", "Ali", "Mehmet", "Ayşe"]

benzersiz = set(liste)
print(benzersiz) # {'Mehmet', 'Ayşe', 'Ali'}
print(len(benzersiz)) # 3

ad = "Süleyman"
yas = 27
sehir = "Trabzon"
boy = 1.82

print(type(ad)) # <class 'str'>
print(type(yas)) # <class 'int'>
print(type(sehir)) # <class 'str'>
print(type(boy)) # <class 'float'>

# yas_str = input("yaşı girin: ")
# print(type(yas_str))

# yas_int = int(yas_str)
# print("10 yıl sonraki yaşı  girin:", yas_int + 10)

sıra = [10, 20, 34, 37, 45, 85, 90]

print(sıra[0])
print(sıra[2:5])

sıra.remove(10)
print(sıra) # [20, 34, 37, 45, 85, 90]

# sıra.append(1)
# print(sıra) # [20, 34, 37, 45, 85, 90, 1]

sıra.pop()
print(sıra) # [20, 34, 37, 45, 85]

sıra.pop(2) # [20, 34, 45, 85]
print(sıra)

sıra[0] = 99
print(sıra) # [99, 20, 34, 37, 45, 85, 90]


ogrenci = {"isim": "zerrin", "soyad": "yıldırım", "yas": 18, "bolum": "uluslararası iliskiler"}

print(ogrenci["isim"])
print(ogrenci["soyad"])
print(ogrenci["yas"])
print(ogrenci["bolum"])

ogrenci["yas"] = 19
print(ogrenci)

del ogrenci["bolum"]
print(ogrenci)

ogrenci["not"] = 100
print(ogrenci)

print(ogrenci.keys())
print(ogrenci.values())
print(ogrenci.items())

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}

print(a.union(b)) # {1, 2, 3, 4, 5, 6, 7, 8}
print(a.intersection(b)) # {3, 4, 5}
print(a.difference(b)) # {1, 2}
