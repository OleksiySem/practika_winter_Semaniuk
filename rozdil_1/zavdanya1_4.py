import math

def calculate_projectile_motion():
    g = 9.81

    print("___ Розрахунок польоту снаряда ___")

    try:
        v0 = float(input("Введіть початкову швидкість (м/с): "))
        angle_deg = float(input("Введіть кут вильоту (градуси): "))
    except ValueError:
        print("Помилка: будь ласка, введіть числові значення.")
        return

    angle_rad = math.radians(angle_deg)

    v0_y = v0 * math.sin(angle_rad)

    total_time = (2 * v0_y) / g

    max_height = (v0_y ** 2) / (2 * g)

    max_range = v0 * math.cos(angle_rad) * total_time

    print("\n--- Результати ---")
    print(f"Повний час польоту: {total_time:.2f} с")
    print(f"Максимальна висота: {max_height:.2f} м")
    print(f"Дальність польоту: {max_range:.2f} м")

    print("\n--- Висота щосекунди ---")
    print(f"{'Час (с)':<10} | {'Висота (м)':<10}")
    print("-" * 25)

    t = 0
    while t <= total_time:

        current_height = (v0_y * t) - (0.5 * g * (t ** 2))

        if current_height < 0:
            current_height = 0.0

        print(f"{t:<10} | {current_height:.2f}")
        t += 1

    if t - 1 != total_time:
        print(f"{total_time:<10.2f} | 0.00 (Падіння)")

if __name__ == "__main__":
    calculate_projectile_motion()