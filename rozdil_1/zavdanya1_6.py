def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

number = 5
print(f"Факторіал {number} дорівнює {factorial(number)}")