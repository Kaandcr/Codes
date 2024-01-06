#Kullanıcıdan ismini alıp ekrana tersten yazan programı yazınız ?

isim= input("İsminizi giriniz: ")
isim = isim[:: -1]
print(isim)
