secim= input("sinema için (1),Tiyatro için (2) yazınız: \n >>>>")
ogrenci=input("Öğrenci misiniz = E/H: \n >>>")
sinema_ücreti=15
tiyatro_ücreti=20

if ogrenci=="E"or "e" and secim=="1":
    indirimli_sinematutari=sinema_ücreti*1/2
    print(f" ödeyeceğiniz ücret{indirimli_sinematutari}")
elif ogrenci=="E" or "e" and secim=="2":
    indirimli_tiyatro=(tiyatro_ücreti)*1/2
    print(f" ödeyeceğiniz ücret{indirimli_tiyatro}")
elif ogrenci=="H" or "h" and secim=="1":
    print(f" ödeyeceğiniz ücret{sinema_ücreti}")
elif ogrenci=="H" or "h" and secim=="2":
    print(f"ödeyeceğiniz ücret{tiyatro_ücreti}")
