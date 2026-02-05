from zavdanya2_6 import *
animals = [Dog(), Cat(), Cow()]

print("--- Звуки тварин ---")
for animal in animals:
    print(f"{type(animal).__name__} каже: {animal.sound()}")# Тут відбувається пізнє зв’язування
