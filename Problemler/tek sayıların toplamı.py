n = int(input(" n sayısı : "))

toplam = 0
for i in range(n):
    if i%2==1:
        toplam+=i
print("Tek sayıların toplamı : ",toplam)
