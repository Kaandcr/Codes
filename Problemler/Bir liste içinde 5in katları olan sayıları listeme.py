sayilar= [15,255,25,75,87,5,8,548,37,34,4543,47,43,]

sayac=0
for sayi in (sayilar):
    if sayi%5==0:
        sayac=sayac+1

print(f"{sayac} tane 5 e bölünen sayı vardır." )
