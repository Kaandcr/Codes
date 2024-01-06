#N den m mye kadar olan sayılardan 7 ye tam bölünenleri bul
# n başlangıç ve m bitiş sayısı kullanıcıdan alınacak

n=int(input("Hangi sayıdan başlayalım : "))
m= int(input("Hangi sayıya kadar 7 ye bölünenleri toplayalım: "))

toplam=0

for i in range(n,m+1):
    if i%7==0:
        toplam +=i
print(toplam)
