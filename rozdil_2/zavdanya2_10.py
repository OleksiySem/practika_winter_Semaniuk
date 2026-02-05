class Car:
    def __init__(self, model: str, year: int, mileage: float):
        self.model = model
        self.year = year
        self._mileage = mileage

    @property
    def mileage(self):
        return self._mileage
    @mileage.setter
    def mileage(self, value):
        if value < 0:
            raise ValueError("Пробіг не може бути від'ємним!")
        if value < self._mileage:
            raise ValueError("Новий пробіг не може бути меншим за поточний (скручування заборонено)!")

        self._mileage = value

my_car = Car("Toyota Camry", 2020, 50000)

print(f"Поточний пробіг: {my_car.mileage} км")

try:
    my_car.mileage = 55000
    print(f"Оновлений пробіг: {my_car.mileage} км")
except ValueError as e:
    print(f"Помилка: {e}")

try:
    my_car.mileage = -100
except ValueError as e:
    print(f" Помилка: {e}")

try:
    my_car.mileage = 20000
except ValueError as e:
    print(f" Помилка: {e}")