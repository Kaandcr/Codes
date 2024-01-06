sayigir=(input("Lütfen bir sayı gir:"))

stringlihali=str(sayigir)

toplam=""

for i in stringlihali:
    toplam =i+toplam
if stringlihali==toplam:
    print("Palindrom")
else:
    print("Palindrom değil")
