a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
if a > b and a>c:
    en_buyuk = a
elif b > a and b > c:
    en_buyuk = b
else:
    en_buyuk = c
print("en buyuk sayi: ",en_buyuk)