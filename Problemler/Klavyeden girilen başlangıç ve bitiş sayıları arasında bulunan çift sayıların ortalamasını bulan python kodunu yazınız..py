toplam=0
sayac=0


baslangicsayi=int(input("Başlangıç sayısı : "))
bitissayi=int(input("Bitiş sayısı : "))

for a in range(baslangicsayi,bitissayi+1):
    if a%2==0:
        toplam+=a
        sayac+=1
print("Çift sayıların ortalaması",toplam/sayac)
