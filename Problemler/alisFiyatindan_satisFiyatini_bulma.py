alis_fiyati = int(input("alis fiyatinizi giriniz: "))
vergi = alis_fiyati*(18/100)
kar_orani = alis_fiyati*(50/100)
satis_fiyati = alis_fiyati + vergi + kar_orani
print(f"aldiginiz urunun satis fiyati {satis_fiyati}dir.")