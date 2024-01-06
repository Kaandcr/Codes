#Kullanıcının istediği büyüklükte bir diziyi
#1-100 arasında rastgele oluşturulmış sayılarla doldurup
#bu sayıların standart sapmasını hesaplayınız

import random

u= int(input("Lütfen dizi uzunluğu giriniz: "))

dizi=[]

for i in range (u):
    dizi.append(random.randint(0,100))

print(dizi)

