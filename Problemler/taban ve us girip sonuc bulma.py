us = int(input("sayinin ussunu giriniz: "))
taban = int(input("sayinin tabanini giriniz: "))
sonuc = 1
for i in range(1, int(us)+1):
    sonuc = sonuc*int(taban)
print(sonuc)
