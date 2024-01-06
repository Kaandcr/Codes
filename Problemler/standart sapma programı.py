x = []
for i in range(5):
   x.append(int(input((str(i+1)+". sayıyı giriniz: "))))
top = 0
for i in range(5):
   top += x[i]
ort = (top/5)
kare_top = 0
for i in range(5):
    kare_top += (x[i]-ort)**2
kare_ort = kare_top/5
ss = kare_ort**0.5
