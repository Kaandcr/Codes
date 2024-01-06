x = int(input("Sayı giriniz:"))

satirsayi = (x*2) + 1

bosluk1 = satirsayi - 2

yildizsayi = 1

for i in range (satirsayi//2):
    print(yildizsayi * "*" + bosluk1 * " " + yildizsayi * "*")
    bosluk1 -= 2
    yildizsayi += 1

bosluk1 = 1
print(satirsayi * "*")
yildizsayi -= 1

for i in range (satirsayi//2):
    print(yildizsayi * "*" + bosluk1 * " " + yildizsayi * "*")
    bosluk1 +=2
    yildizsayi-=1
