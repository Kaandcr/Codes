def fibonacci(n):
    fib_list = [1, 1]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list


fibonacci_numbers = fibonacci(10)


toplam = sum(fibonacci_numbers)

print(f"1'den 10'a kadar olan Fibonacci sayılarının toplamı: {toplam}")

