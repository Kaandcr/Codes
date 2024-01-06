saat=int(input("Saati giriniz: "))
dakika=int(input("Dakikayı giriniz: "))


if dakika==0:
    print(f"Saat {saat}")
elif dakika==15:
    print(f"{saat} çeyrek geçiyor")
elif dakika==30:
    print(f"saat {saat}buçuk")
elif dakika>0 and dakika<30:
    print(f" saat {saat}i {dakika}geçiyor")
elif dakika==45:
    print(f"{saat+1}e çeyrek var")
    if saat==23:
        print(f"Saat 00'a çeyrek var")


elif dakika>30 and dakika<60:
    if saat == 23:
        print(f"00.a {60- dakika} var.")
    else:
        print(f"{saat + 1}ya {60-dakika} var")y



