toplamlari = 0
sayi = int(input("bir sayi giriniz: "))
for i in range(1,sayi):
    if sayi % i == 0:
        toplamlari += i
if toplamlari == sayi:
    print(f"{sayi} bir mükemmel sayıdır")
else:
    print(f"{sayi} bir mükemmel sayı degıldır")


toplamlari = 0
sayi = int(input("bir sayi giriniz: "))
for i in range(1,sayi):
    if sayi % i == 0:
        toplamlari += i
if toplamlari == sayi:
    for a in range(1,sayi):
        if sayi % a == 0:
            print(f"{a} sayısı {sayi} ın carpanlarından bırıdır")