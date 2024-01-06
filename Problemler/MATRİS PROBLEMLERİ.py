#
# İKİ MATRİSİN ÇARPIMI BULAN PROGRAM
#
# def matris_carpimi(matris1, matris2):
#
#     m1_satir = len(matris1)
#     m1_sutun = len(matris1[0])
#
#
#     m2_satir = len(matris2)
#     m2_sutun = len(matris2[0])
#
#
#     sonuc_matrisi = [[0 for _ in range(m2_sutun)] for _ in range(m1_satir)]
#
#
#     for i in range(m1_satir):
#         for j in range(m2_sutun):
#             for k in range(m1_sutun):
#                 sonuc_matrisi[i][j] += matris1[i][k] * matris2[k][j]
#
#     return sonuc_matrisi
#
#
# matris1 = [[1, 1, 2]
#         , [2, 2, 2]]
#
# matris2 = [[2, 1],
#            [1,0],
#            [1,0]]
#
#
# sonuc = matris_carpimi(matris1, matris2)
#
# for satir in sonuc:
#     print(satir)

# import random

# Girilen N değerine göre NxN boyutlu bir matrisin hücrelerine 1 den NxN'e kadar sayıları yerleştir.

# def matris_olustur_ve_doldur(N):
#     matris = [[0] * N for _ in range(N)]  # NxN boyutunda sıfırlardan oluşan bir matris oluştur
#
#     sayac = 1
#     for i in range(N):
#         for j in range(N):
#             matris[i][j] = sayac
#             sayac += 1
#
#     return matris
#
# N = int(input("Matris boyutunu girin (N): "))
#
# # Matrisi oluştur ve doldur
# matris = matris_olustur_ve_doldur(N)
#
# for satir in matris:
#     print(satir)


# 0-1 değerlerini içeren bir matristeki nesnenin kenarlarını hesapla.
#
#
# def nesne_alanini_hesapla(matris):
#     alan = 0
#     m = len(matris)
#     n = len(matris[0])
#
#     for i in range(m):
#         for j in range(n):
#             if matris[i][j] == 1:
#                 alan += 1
#
#     return alan
#
#
# ornek_matris = [
#     [0, 1, 0, 1, 0],
#     [1, 1, 0, 0, 1],
#     [0, 0, 0, 1, 0],
#     [1, 0, 1, 0, 1],
# ]
#
# nesne_alani = nesne_alanini_hesapla(ornek_matris)
#
#
# print("Nesnenin Alanı:", nesne_alani)






#MATRİSİ N KAT BÜYÜTEN PROGRAM
# def matrisi_n_kat_buyut(matris, n):
#     m = len(matris)  # Matrisin satır sayısı
#     n_original = len(matris[0])  # Matrisin sütun sayısı
#
#     # Yeni matrisin boyutlarını hesapla
#     yeni_m = m * n
#     yeni_n = n_original * n
#
#     # Yeni matrisi oluştur ve başlangıçta tüm elemanları sıfır yap
#     yeni_matris = [[0] * yeni_n for _ in range(yeni_m)]
#
#     # Her elemanın bulunduğu konumu n kat büyüt
#     for i in range(m):
#         for j in range(n_original):
#             eleman = matris[i][j]
#             for k in range(n):
#                 for l in range(n):
#                     yeni_matris[i * n + k][j * n_original + l] = eleman
#
#     return yeni_matris
#
# # Örnek matris
# ornek_matris = [
#     [1, 2],
#     [3, 4],
# ]
#
# # Matrisi 3 kat büyüt
# n_kat = 2
# yeni_matris = matrisi_n_kat_buyut(ornek_matris, n_kat)
#
# # Sonucu ekrana yazdır
# for satir in yeni_matris:
#     print(satir)









# rastgele MATRİS üret  TRANSPOZUNU AL
# random.randint
#
#
# satir=int(input("Kaç satır olsun:"))
# sütun=int(input("Kaç sütun olsun:"))
#
#
# m1=[[0 for x in range(satir)]  for y in range(sütun)]
# mt=[[0 for x in range(satir)]  for y in range(sütun)]
#
#
# for i in range(satir):
#     for j in range(sütun):
#         m1[i][j]=random.randint(0,9)
#         mt[j][i]=m1[i][j]
#
# for c in range(satir):
#     print("Oluşan matris= ",m1[c])
#
# for d in range(sütun):
#     print("Matrisin transpozu=",mt[d])











































