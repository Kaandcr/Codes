sayi = int(input("uc basamakli bir sayi giriniz: "))
yuzler_basamagi = sayi//100
ikibasamakli = sayi-yuzler_basamagi*100
onlar_basamagi = ikibasamakli//10
birler_basamagi = sayi - yuzler_basamagi*100 - onlar_basamagi*10
print(f"girdiginiz sayininn\nyuzler basamagi: {yuzler_basamagi}\nonlar basamagi: {onlar_basamagi}\nbirler basamagi:{birler_basamagi}")