#Kullanıcının istediği kadar sayıyı kullanıcıdan alarak bir diziye aktaran


dizi = []
toplam = 0
adet = int(input("Kaç adet sayı girmek istiyorsunuz : "))

for i in range (adet):
    dizi.append(int(input("Sayıyı giriniz")))
    toplam += i
print(f"Girdiğiniz sayıların toplamı {toplam}dır.")

a=toplam/adet
print(f"girdiğiniz sayıların ortalaması {a}dır ")
