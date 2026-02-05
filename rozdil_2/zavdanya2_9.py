from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._hunger = 100

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def specific_behavior(self):
        pass

    def eat(self, food_amount):
        self._hunger -= food_amount
        if self._hunger < 0:
            self._hunger = 0
        print(f"{self.name} їсть. Рівень голоду знизився до {self._hunger}.")

    def get_hunger_status(self):
        return self._hunger
class Lion(Animal):
    def make_sound(self):
        return "ГРРРР! (грізний рик)"

    def specific_behavior(self):
        return "полює на здобич у вольєрі."
    def eat(self, food_amount):
        print(f"{self.name} розриває м'ясо.")
        super().eat(food_amount)
class Monkey(Animal):
    def make_sound(self):
        # --- ПОЛІМОРФІЗМ ---
        return "У-у-у, а-а-а! (веселий крик)"

    def specific_behavior(self):
        return "гойдається на ліанах."

    def eat(self, food_amount):
        print(f"{self.name} чистить банан.")
        super().eat(food_amount)
class Zookeeper:
    def __init__(self, name):
        self.name = name

    def check_animal(self, animal: Animal):
        print(f"\n[{self.name}] підходить до {animal.name}...")
        print(f"Тварина каже: {animal.make_sound()}")
        print(f"Тварина {animal.specific_behavior()}")

        if animal.get_hunger_status() > 50:
            print(f"[{self.name}] бачить, що {animal.name} голодний.")
            self.feed_animal(animal)
        else:
            print(f"{animal.name} не хоче їсти.")

    def feed_animal(self, animal: Animal):
        print(f"[{self.name}] дає їжу для {animal.name}.")
        animal.eat(40)

def main():
    simba = Lion("Сімба", 5)
    abu = Monkey("Абу", 2)
    keeper = Zookeeper("Петро")
    zoo_animals = [simba, abu]

    print("--- ПОЧАТОК РОБОЧОГО ДНЯ В ЗООПАРКУ ---")
    for animal in zoo_animals:
        keeper.check_animal(animal)

    print("\n--- ПЕРЕВІРКА ПІСЛЯ ГОДУВАННЯ ---")
    for animal in zoo_animals:
        print(f"{animal.name}: Рівень голоду = {animal.get_hunger_status()}")

if __name__ == "__main__":
    main()