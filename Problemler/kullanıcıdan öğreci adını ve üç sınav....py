#Kullanıcıdan öğrenci adını ve üç sınav notu girdirin
#kullanıcı q tuşuna basana kadar bu işlemi tekrarla
#ardından öğrenci not bilgilerini ekrana yazdırınız
#her öğrencinin adını notlarını ve ortalama notunu göster

while True:
    ogrenciadi = input("Öğrenci adını girin (q'ya basarak çıkış yapın): ")

    if ogrenciadi.lower() == 'q':
        break


    sinav1 = float(input("1. sınav notunu girin: "))
    sinav2 = float(input("2. sınav notunu girin: "))
    sinav3 = float(input("3. sınav notunu girin: "))

    ortalama  = (sinav1+ sinav2 + sinav3) / 3


    print(f"\nÖğrenci Adı: {ogrenciadi}")
    print(f"Sınav 1 Notu: {sinav1}")
    print(f"Sınav 2 Notu: {sinav2}")
    print(f"Sınav 3 Notu: {sinav3}")
    print(f"Ortalama Not: {ortalama}\n")

