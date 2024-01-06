def kelime_sayaci(metin,kelime):
    kelimeler=metin.split()
    sayac=0
    for i in kelimeler:
        if i ==kelime:
            sayac+=1
    return sayac
metin=input("Bir metin giriniz: ")
kelime=input("Saymak istediğiniz kelimeyi giriniz")
sayi= kelime_sayaci(metin,kelime)
print(f"Seçtiğiniz {kelime}si {sayi} kere kullanılmıştır:")
