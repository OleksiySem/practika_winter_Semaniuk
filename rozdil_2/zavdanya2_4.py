class Car:
    def __init__(self, marka, rik_vypusku, probih):
        self.marka = marka
        self.rik_vypusku = rik_vypusku
        self.probih = probih

    def drive(self, km):
        if km > 0:
            self.probih += km
            print(f"Авто проїхало {km} км. Новий пробіг: {self.probih} км.")
        else:
            print("Кількість кілометрів повинна бути додатною!")

    def info(self):
        print(f"--- Інформація про автомобіль ---")
        print(f"Марка: {self.marka}")
        print(f"Рік випуску: {self.rik_vypusku}")
        print(f"Поточний пробіг: {self.probih} км")
        print("-" * 30)

    def __str__(self):
        return f"{self.marka} ({self.rik_vypusku} р.в.) - {self.probih} км"

my_car = Car("Toyota Camry", 2020, 45000)

my_car.info()

my_car.drive(150)

my_car.info()

print(f"Короткий опис: {my_car}")