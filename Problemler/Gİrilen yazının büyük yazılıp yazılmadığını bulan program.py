alfabe = []

for i in 'QWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ':
    alfabe.append(i)

yazi = input("Bir yazı yazınız: ")

if yazi[0] in alfabe:
    print(f"Yazısı büyük harf ile başlar: {yazi}")
else:
    print(f"Yazısı büyük harfle başlamıyor: {yazi}")
