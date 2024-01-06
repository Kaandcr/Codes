# list=["ben","Kaan","Memnun","Oldum"]
# a="m"
# print((type(list)))
#
# a.upper()
# print(a.upper())



# def sayHello(name="user"):
#     return "Hello" + name
# msg=sayHello("kaan")
# msg=sayHello("Ada")
#
# print(msg)
#
#
# def total(num1,num2):
#     return num1 + num2
# result=total(5,20)
# print(result)



# def yashesapla(dogumyili):
#     return 2023-dogumyili
#
#
# def Emeklilik(dogumyili,isim):
#     yas=yashesapla(dogumyili)
#     emeklilik=65-yas
#     if emeklilik>0:
#         print(f"Emekliliğinize {emeklilik} yıl kaldı")
#     else:
#         print("Zaten emekli oldunuz")
#
# Emeklilik(2002,"Kaan")



# def Kelime(kelimegir,kackez):
#     for i in range(kackez):
#         print(kelimegir)
# Kelime("Kaan",5)

# def Listeyecebir(*params): #* işareti sınırsız bilgi için kullanılır
#     liste=[]
#
#     for param in params:
#         liste.append(param)
#     return liste
# result=Listeyecebir("a",2,4,6,"Allah")
# print(result)




#gönderilen iki sayının arasındaki tüm asal sayıları bulun
# def asalsayibul(sayi1,sayi2):
#     liste=[]
#     for sayi in range(sayi1,sayi2+1):
#         if sayi>1:
#             for i in range(2,sayi):
#                 if sayi % i == 0:
#                     break
#             else:
#                 liste.append(sayi)
#     return liste
# print(asalsayibul(2,10))

#kendisine gönderilen bir sayının tam bölenlerini bulan program


# def tambölenler(sayi):
#     liste=[]
#     for i in range(1,sayi+1):
#         if sayi%i==0:
#             liste.append(i)
#
#     return (f"bölenleri : {liste}")
#
# print(tambölenler(15))
#


#küpünü alan program

# def küpal(sayi):
#     a=sayi**3
#     return a
# print(küpal(5))


def faktoriyel_hesapla(sayi):
    if sayi == 0 or sayi == 1:
        return 1
    else:
        return sayi * faktoriyel_hesapla(sayi - 1)

def faktoriyel_aralik_bul(baslangic, bitis):
    for i in range(baslangic, bitis + 1):
        print(f"{i}! = {faktoriyel_hesapla(i)}")

baslangic_sayisi = int(input("Başlangıç sayısını girin: "))
bitis_sayisi = int(input("Bitiş sayısını girin: "))


faktoriyel_aralik_bul(baslangic_sayisi, bitis_sayisi)


