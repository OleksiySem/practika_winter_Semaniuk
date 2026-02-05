import math

def solve_quadratic():
    print(" Розв'язування квадратного рівняння ax^2 + bx + c = 0 ")

    try:
        a = float(input("Введіть коефіцієнт a: "))
        b = float(input("Введіть коефіцієнт b: "))
        c = float(input("Введіть коефіцієнт c: "))
    except ValueError:
        print("Помилка! Будь ласка, вводьте лише числа.")
        return

    if a == 0:
        print("Це не квадратне рівняння, оскільки a = 0.")
        if b != 0:
            x = -c / b
            print(f"Це лінійне рівняння. Корінь x = {x}")
        else:
            print("Коренів немає або їх безліч (залежно від c).")
        return

    D = b ** 2 - 4 * a * c
    print(f"Дискримінант (D) = {D}")

    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print(f"Рівняння має два корені:\n x1 = {x1}\n x2 = {x2}")
    elif D == 0:
        x = -b / (2 * a)
        print(f"Рівняння має один корінь:\n x = {x}")
    else:
        print("Дискримінант менше нуля. Дійсних коренів немає.")

if __name__ == "__main__":
    solve_quadratic()