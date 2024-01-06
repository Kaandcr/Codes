birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]

# Kullanıcıdan 4 basamaklı bir sayı girişi alınır
sayi = int(input("Lütfen 4 basamaklı bir sayı giriniz: "))

# Sayıyı basamaklarına ayırma
binler = sayi // 1000
yuzler = (sayi % 1000) // 100
onlar_basamagi = (sayi % 100) // 10
birler_basamagi = sayi % 10

# Yazı ile temsil etme
yazi = birler[binler] + " Bin " + onlar[yuzler] + " " + birler[onlar_basamagi] + " " + birler[birler_basamagi]

# Sonucu ekrana yazdırma
print("Sayının yazılışı:", yazi)
