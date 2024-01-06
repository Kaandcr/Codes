import random

satir_gir=int(input("Kaç satırdan oluşsun:\n>>> "))
sütun_gir=int(input("Kaç Sütundan oluşsun:\n>>> "))



m1= [[0 for x in range(satir_gir)]  for y in range(sütun_gir)]
mt= [[0 for x in range(satir_gir)]  for y in range(sütun_gir)]


for i in range(satir_gir):
    for j in range(sütun_gir):
        m1[i][j]=random.randint(0,9)
        mt[j][i]=m1[i][j]

for b in range(satir_gir):
    print(m1[b])

print()

for c in range(sütun_gir):
    print(mt[c])

