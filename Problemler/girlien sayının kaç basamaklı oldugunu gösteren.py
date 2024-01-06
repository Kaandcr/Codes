sayi = int(input("bir sayı giriniz: "))
sayac = 0
while sayi>0:
    sayi = sayi//10
    sayac+=1
print(sayac)