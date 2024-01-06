sayi=int(input("Lütfen sayı giriniz : "))
x =[1,2,3,4,5,6,7,8,9,123,25,25,26,126,32,6,473,47,4357,64,56432,5,32]


kontrol =0


for i in x:
    if i ==sayi:
        kontrol=1
        break

if kontrol== 0:
    print("Listede yok")

else:
    print("Listede var")


