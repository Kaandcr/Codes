sayilar = []
for i in range(5):
    sayi = int(input(f"{i+1}. sayıyı giriniz: "))
    sayilar.append(sayi)



i =1
for sayi in sayilar:
    yildizlar = "*" * (sayi // 100)
    kalan = sayi % 100
    if kalan > 0:
        yildizlar += "*"
    print(f"{i}. sayı: {yildizlar}")
i+=1
