print("Bir sayı giriniz : ")
sayi = int(input())

temp = sayi
uzunluk = len(str(sayi))
toplam = 0
while sayi>0:
    rem = sayi%10
    toplam = toplam + (rem ** uzunluk)
    sayi = int(sayi/10)

if toplam==temp:
    print("\n" +str(temp)+ " sayısı Armstrong sayıdr.")
else:
    print("\n" +str(temp)+ " sayısı Armstrong sayı değildir.")
