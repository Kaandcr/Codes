list=[]

while True:
    sayigir=input("Sayı giriniz: ") #125
    if sayigir=="q" or sayigir=="Q":
        break
    if int(sayigir)>=0 and int(sayigir)<=9:
        list.append(sayigir)

toplam=""

for i in list:
    toplam=toplam + i
karekök=int(toplam)**0.5

print(f"Sayının karekök {karekök}")
