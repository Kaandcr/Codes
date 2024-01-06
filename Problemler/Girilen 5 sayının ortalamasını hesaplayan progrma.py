x=[]
for i in range(5):
    x.append(int(input(str(i+1)+ ". Sayıyı giriniz : ")))
    

toplam=0
for i in range(5):
    toplam+=x[i]
print(toplam/5)