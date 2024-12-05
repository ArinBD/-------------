def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(6)
print(f"Факториал 6 равен: {result}")