
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


fibonacci_liste = [] 
i = 0 
while True: 
    fib = fibonacci(i) 
    if fib > 1000: 
        break 
    fibonacci_liste.append(fib) 
    i += 1 


print("0 ile 1000 arasındaki Fibonacci sayıları:")
for sayi in fibonacci_liste:
    print(sayi)

