#kullanıcıdan ismini ve soyismini alarak içerisinde
#kaç adet sesli ve kaç adet sessiz harf olduğunu bulan program yazınız


sesli="aıoueiöü"
sayac=0

a=input("Kelime giriniz: ")
for harf  in a :
    if harf in sesli:
        sayac+=1
print(sayac)









