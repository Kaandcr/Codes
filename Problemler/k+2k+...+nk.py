n = int(input("bir n degeri giriniz: "))
k = int(input("bir k degeri giriniz: "))
def toplam_hesapla(n, k):
    toplam = 0
    for i in range(n,n+1):
        toplam += i * k
    return toplam
print(f"girdiginiz degerlere gore sonuc {toplam_hesapla(n,k)} dir")