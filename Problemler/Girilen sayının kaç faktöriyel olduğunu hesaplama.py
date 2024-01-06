def faktöriyel_bul(sayi):
    faktöriyel=1
    for i in range(1,sayi+1):
        faktöriyel*=i
    return faktöriyel


girilensayi=int(input("Sayi giriniz: "))

sonuc=faktöriyel_bul(girilensayi)

print(f"girilen sayi {girilensayi}!={sonuc}")


