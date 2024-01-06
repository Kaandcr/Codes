
liste = []
sayi =""
while True:
    rakam = input("rakam giriniz: ")
    if rakam == "q":
        break
    elif int(rakam) >= 0  and int(rakam)<10:
        liste.append(rakam)
for i in liste [::-1]:
    sayi += i
karekok = int(sayi) ** 0.5
print(f"Sayi = {sayi}, karekökü={karekok}")






