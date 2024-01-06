def harf_notunu_hesapla(vize,final):
    toplam=vize*0.40 + final * 0.60
    if toplam >= 70 and toplam <100:
        return "A"
    elif toplam > 49:
        return "B"
    elif toplam> 29:
        return "C"
    else:
        return"D"

print(harf_notunu_hesapla(12,65))


