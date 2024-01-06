asal = []
for sayi in range (1,101):
    if sayi > 1:
        for i in range(2,sayi):
            if sayi % i == 0:
                break
        else:
            asal.append(sayi)
print("toplam sayı",len(asal))