#Kullanıcının girdiği 2 sayıyı toplayan ve toplam sonucu
#40 ile 50 arasında ise ekrana  bildin geç
#yazdıran python kodlarını yazdırınız



sayi1=int(input("Lütfen 1. sayıyı giriniz : "))

sayi2= int(input("Lütfen 2. sayıyı giriniz : "))

toplam = sayi1+sayi2

if toplam>40 and toplam<50:
    print("Bildin geç")


else:
    print("yapamadın brom")
