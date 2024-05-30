def fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for number in fibonacci(10):
    print(number)
# Вывод: 1 1 2 3 5 8 13 21 34 55
