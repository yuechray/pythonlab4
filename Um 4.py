def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов {func.__name__} с args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for number in fibonacci(10):
    print(number)
# Вывод: Вызов fibonacci с args=(10,), kwargs={}
#        1 1 2 3 5 8 13 21 34 55
