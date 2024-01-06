def asal_mi(sayi):
    if sayi < 2:
        return False
    for i in range(2, int(sayi**0.5) + 1):
        if sayi % i == 0:
            return False
    return True

def ilk_n_asal_sayi(n):
    asal_sayilar = []
    sayi = 2  # Asal sayıları bulmaya 2'den başlıyoruz

    while len(asal_sayilar) < n:
        if asal_mi(sayi):
            asal_sayilar.append(sayi)
        sayi += 1

    return asal_sayilar

# İlk 5 asal sayıyı bulmak için fonksiyonu çağır
ilk_bes_asal = ilk_n_asal_sayi(11)

# Sonucu ekrana yazdır
print("İlk 5 asal sayı:", ilk_bes_asal)
