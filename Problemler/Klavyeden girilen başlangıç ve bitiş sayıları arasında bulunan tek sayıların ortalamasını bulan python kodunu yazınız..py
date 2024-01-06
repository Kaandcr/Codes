toplam=0

sayac=0

baslangicsayi=int(input("Başlangıç sayısı: "))

bitissayi=int(input("Bitiş sayısı: "))

for i in range(baslangicsayi,bitissayi+1):
    if i%2==1:
        toplam=toplam+i
        sayac+=1
print("Ortalama" , toplam/sayac)

