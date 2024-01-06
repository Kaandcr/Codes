fiyat = int(input("aldiginiz urunun fiyatini giriniz: "))
kdv = int(input("kdv oranini giriniz: "))
kdv_tutari = (fiyat*kdv)/100
toplam_tutar = kdv_tutari + fiyat
print(f"aldiginiz urunun kdv dahil toplam tutari: {toplam_tutar}")
