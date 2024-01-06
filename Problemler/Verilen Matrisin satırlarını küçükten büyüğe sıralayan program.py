try:
    # Kullanıcıdan matris boyutlarını al
    satir_sayisi = int(input("Matrisin satır sayısını girin: "))
    sutun_sayisi = int(input("Matrisin sütun sayısını girin: "))

    # Matrisi oluştur
    matris = []
    for i in range(satir_sayisi):
        row = []
        for j in range(sutun_sayisi):
            eleman = float(input(f"Matrisin {i+1}. satır, {j+1}. sütun elemanını girin: "))
            row.append(eleman)
        matris.append(row)

    # Satırları sırala
    for i in range(satir_sayisi):
        matris[i].sort()

    # Sonuçları göster
    print("\nMatris:")
    for row in matris:
        print(row)

except ValueError:
    print("Hatalı giriş. Lütfen sayısal değerler girin.")
