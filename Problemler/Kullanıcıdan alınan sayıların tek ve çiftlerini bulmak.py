s=0
teksayac=0
ciftsayac=0
tektoplam=0
cifttoplam=0

for sayi in range(1,11):
    s= int(input("Lütfen sayıyı giriniz: "))
    if sayi %2==1:
        teksayac+=1
        tektoplam+=s
    else:
        ciftsayac+= 1
        cifttoplam+=s
print(teksayac,"adet tek sayı vardır, toplamları ", tektoplam)
print("Tek sayıların ortalaması", tektoplam/teksayac)

print(ciftsayac,"adet cift sayı vardır, toplamları ", cifttoplam)
print("Tek sayıların ortalaması", cifttoplam/cifttoplam)


