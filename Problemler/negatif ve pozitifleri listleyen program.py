negatif =[]
pozitif = []

for i in range(1,10):
    sayi = int(input("bir sayı giriniz:"))
    if sayi < 0:
        negatif.append(sayi)
    elif sayi>0:
        pozitif.append(sayi)

print(f"girdiğiniz sayılardaki negatif sayılar {negatif}\npozitif sayılar{pozitif}\n")