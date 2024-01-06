satir=int(input("kaç satırlık yıldız oluşturulsun:"))
for i in range(1,satir+1):
    if i==1:
        print(" "*((2*satir)-i+1)+"*")
    else:
        print(" "*((2*satir)-i)+"*",end=(i-1)*" "+" "*i +"*")
        print()
