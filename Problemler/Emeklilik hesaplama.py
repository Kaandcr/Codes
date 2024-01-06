
def yasHesapla(dogumyili):
    return 2023-dogumyili


def emeklilike_kac_yil_kaldi(dogumyili,isim):
    yas=yasHesapla(dogumyili)
    emeklilik=65-yas

    if emeklilik>0:
        print(f"emekliliğinize {emeklilik} yıl kaldı")

    else:
        print("Zaten emekli oldunuz")


emeklilike_kac_yil_kaldi(2023,"Ali")
