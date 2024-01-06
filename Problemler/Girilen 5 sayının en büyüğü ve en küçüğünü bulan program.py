listem = []

for i in range(5):
    gir = int(input("Lütfen bir sayı giriniz: "))
    listem.append(gir)

a = max(listem)
b = min(listem)

print("En büyük sayı:", a)
print("En küçük sayı:", b)
