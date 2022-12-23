#1->kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız?

kelime = input("kelime giriniz: ")
kackezyazilsin = int(input("kaç defa yazılsın: "))

def fon(kelime,kackezyazilsin):
    for i in range(kackezyazilsin):
        print(kelime)
fon(kelime,kackezyazilsin)

#2->dikdötgenin alan ve çevresini hesaplayan fonksiyonu yazınız?

kisaKenar = int(input("Dikdörtgenin kısa kenarını giriniz: "))
uzunKenar = int(input("Dikdörtgenini uzun kenarını giriniz: "))

def hesap(kisaKenar,uzunKenar):
    alan = kisaKenar*uzunKenar
    cevre = (kisaKenar+uzunKenar)*2
    return f"Dikdörtgenin alanı {alan} çevresi {cevre}"
sonuc= hesap(kisaKenar,uzunKenar)
print(sonuc)

#3->yazı tura uygulamasını fonksiyon kullanarak yapınız random modülü
para= ["yazı","tura"]
def yaziTuraAt():
    import random
    return random.choice(para)
sonuc = yaziTuraAt()
print(sonuc)

#4-> kendisine göderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız?

def asalSayiBul(sayi1,sayi2):
    
    for sayi in range(sayi1,sayi2+1):
        if(sayi>1):
            for i in range(2,sayi):
                if sayi%i==0:
                    break
            else:
                 print(sayi)
                
asalSayiBul(2,86)  

#5->kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren bir fonksiyon yazınız

def tamBolen(sayi):
    bolenler = []
    for i in range(1,sayi+1):
        if sayi%i==0:
            bolenler.append(i)
    print(bolenler)
tamBolen(60)
            

