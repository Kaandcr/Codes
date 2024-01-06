
'''
arabalar = ["BMW","Mercedes","Opel","Mazda"]

a=len(arabalar)
print(a)
'''

'''

renkler= ["Mavi","sarı","Kahverengi","Kumral"]
renkler2=["Turuncu ","Pembe"]

'''



#list.append(renkler, "a")
#append komutu diziye o kelimeyi ekler


#renkler.insert(2,"gri")  2.yere gri ekle

#renkler.remove("sarı") sarıyı siler


#renkler.extend(renkler2)
#(sadece listenin elemanlarını ekler [] olmadan)


#silinen = renkler.pop(0-2)
#renkler.pop komutu içindeki değişkenleri siler
#print(renkler)
#print(silinen) der isek hangi şey silinmiş onu gösterir

'''
renkler. reverse()
print(renkler)'''
'''
renkler.sort(reverse=True)
print(renkler)
liste 2 = sorted(renkler)
print(renkler)
'''



renkler = ["siyah","Beyaz","Sarı","Mavi","Yeşil"]

print(min(renkler))
print(max(renkler))

alfabetik olarak en büyük ve en küçük olan elemanları yazdırır.

'''
'''
BURASI ÇOKKKKKKKKKKKKKKKKKKKKKKK ÖNEMLİİİİİİİİİİİİİİİİİİİİİİİİİİİİİİİİİİ
renkler = ["siyah","Beyaz","Sarı","Mavi","Yeşil"]

print(list(enumerate(renkler,start=1)))
ÇIKTISI BÖYLE OLUYOR : [(1, 'siyah'), (2, 'Beyaz'), (3, 'Sarı'), (4, 'Mavi'), (5, 'Yeşil')]

print("gri" in renkler)
false çıktısı verir 
'''
'''
renkler = ["siyah","Beyaz","Sarı","Mavi","Yeşil"]
stringrenkler="".join(renkler)
print(stringrenkler)


