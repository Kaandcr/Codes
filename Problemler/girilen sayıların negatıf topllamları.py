negatif_toplamları = 0
for i in range(0,5):
    sayi = int(input(f"{i+1}. sayıyı giriniz: "))

    if sayi < 0:
        negatif_toplamları += sayi
print(f"girdiginiz sayıların negatıf olanların toplamı {negatif_toplamları}dir.")