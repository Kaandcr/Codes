import math

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

delta = b**2 - (4*a*c)

print("Delta: ", delta)

if delta > 0:
    kök1 = (-b + math.sqrt(delta)) / (2*a)
    kök2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"Köklerden birincisi {kök1} ve ikincisi {kök2}dir.")

elif delta < 0:
    print("Reel kök yoktur")

elif delta == 0:
    kök = -b / (2*a)
    print(f"Çakışık iki kök vardır. Kök ise : {kök} dir ")

