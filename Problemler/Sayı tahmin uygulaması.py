import random
sayi = random.randint(0,10)
can = 5
isim = input("isminiz: ")

for i in range(5):
    tahmin = int(input("0 ile 10 arasında bir sayı tahmin et: "))
    if sayi == tahmin:
        print("doğru tahmin ettiniz.")
        print(f"Kalan tahmin etme hakkınız: {can}")
        break
    else:
        if sayi<tahmin:
            print("Lütfen tekrar deneyiniz. Tahmin ettğiniz sayı düşürünüz.")
            print(f"Kalan tahmin etme hakkınız: {can}")
            print(f"Yanlış tahmin  {isim}")
        if sayi>tahmin:
            print("Lütfen tekrar deneyiniz. Tahmin ettğiniz sayı Yükseltiniz.")
            print(f"Kalan tahmin etme hakkınız: {can}")
            print(f"Yanlış tahmin  {isim}")
        can -= 1
if can == 0:
    print(f"Doğru sayı:{sayi}")
