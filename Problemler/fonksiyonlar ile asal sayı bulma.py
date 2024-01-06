#ASAL SAYI BULMA

giris=int(input("Kaç asal sayı listeleyelim:\n>>>"))

asalsayilar=[]

sayi=2

while len(asalsayilar)<giris:
    asal=1
    for bolen in range(2,sayi):
        if sayi%bolen==0:
            asal=0
            break
    if asal:
        asalsayilar.append(sayi)
    sayi+=1
print(asalsayilar)
