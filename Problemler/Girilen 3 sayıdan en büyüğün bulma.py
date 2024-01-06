s1=int(input("1. sayıyı giriniz"))
s2=int(input("2. sayıyı giriniz"))
s3=int(input("3. sayıyı giriniz"))

if s1 >s2 and s1>s3:
    print("En büyük sayı : " f"{s1}dir")
if s2>s1 and s2>s3:
    print("En büyük sayı : " f"{s2}dir")

if s3 > s1 and s3> s2:
    print("En büyük sayı : " f"{s3} dir")
