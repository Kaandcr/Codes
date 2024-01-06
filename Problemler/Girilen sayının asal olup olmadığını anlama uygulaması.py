
sayac=0
sayi=int(input('Bir Sayı Giriniz: '))
for i in range(2,(sayi)):
  if((sayi)%i==0):
    sayac+=1
    break
if(sayac!=0):
  print("Girilen Sayı Asal Değil")
else:
  print("Girilen Sayı Asal")
