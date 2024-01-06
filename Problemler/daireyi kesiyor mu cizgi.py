import math
#cizgi = ax + by + c    daire = (dx, dy)
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
dx = int(input("dx:"))
dy = int(input("dy:"))
r = int(input("r:"))
d = abs(a*dx + b*dy + c) / sqrt(a**2 + b**2)
if d>r:
    print("kesme yok")
elif d == r:
    print("teget")
else:
    print("KESME VAR")
