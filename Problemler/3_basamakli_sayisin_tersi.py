print("Merhabalar girdiginiz 3 basamakli sayiyi tersine ceviren programa hosgeldiniz !!!")
sayi = int(input("uc basamakli bir sayi giriniz: "))
a = sayi//100
onlar = sayi - 100*a
b = onlar//10
c = sayi - a*100 - b*10
yeni_sayi = c*100 + b*10 + a
print(f"yazdiginiz sayinin tersi {yeni_sayi}'dir")
