sayi = int(input("Lütfen bir sayı giriniz: "))


sayac =0


for i in range(1, sayi + 1):
    if sayi % i == 0:
        sayac+=1

print(f"Tam bölen sayısı : {sayac} dır ")

