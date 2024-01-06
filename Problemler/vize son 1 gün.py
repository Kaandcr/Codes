

list=[]
newlist=[]
while True:
    sayi=input("Lütfen bir rakam giriniz: ")
    if sayi=="q":
            break
    elif int(sayi) <9 and int(sayi)>0:
        list.append(sayi)


sayac=0
for i in list:
    x=len(list)
    ters=list[(x-1)-sayac]
    sayac+=1
    newlist.append(ters)

toplam=""

for i in newlist:
    toplam+=i
karekok=int(toplam)**0.5
print(karekok)
