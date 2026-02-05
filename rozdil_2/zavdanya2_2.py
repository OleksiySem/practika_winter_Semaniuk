class Student:
    def __init__(self, name, group, average_score):
        self.name = name
        self.group = group
        self.average_score = average_score

    def show_info(self):
        print(f"Студент: {self.name}")
        print(f"Група: {self.group}")
        print(f"Середній бал: {self.average_score}")
        print("-" * 20)

student1 = Student("Олександр Іваненко", "ІПЗ-21", 10.5)
student2 = Student("Марія Петренко", "ІПЗ-12", 9.6)
student3 = Student("Дмитро Коваленко", "ІПЗ-23", 8.0)

student1.show_info()
student2.show_info()
student3.show_info()