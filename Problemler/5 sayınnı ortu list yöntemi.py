x = []
for i in range(5):
   x.append(int(input((str(i+1)+". sayıyı giriniz: "))))
top = 0
for i in range(5):
   top += x[i]
ort = (top/5)
print(f"girlen sayıların ortallaması {ort}")
