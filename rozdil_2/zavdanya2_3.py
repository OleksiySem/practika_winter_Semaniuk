def analyze_student_grades(students_data):

    average_scores = {}
    all_unique_grades = set()

    for name, grades in students_data.items():

        all_unique_grades.update(grades)

        if len(grades) > 0:
            avg = sum(grades) / len(grades)
            average_scores[name] = round(avg, 2)
        else:
            average_scores[name] = 0.0

    return average_scores, all_unique_grades

students_input = {
    "Олена": [85, 90, 92, 88],
    "Андрій": [70, 75, 70, 60],
    "Марія": [95, 100, 95, 98],
    "Петро": [85, 85, 85, 85]
}

averages, uniques = analyze_student_grades(students_input)

print("--- Середні бали студентів (dict) ---")
for student, avg in averages.items():
    print(f"Студент: {student:10} | Середній бал: {avg}")

print("\n--- Унікальні оцінки по групі (set) ---")
print(sorted(uniques))

print(f"\nКількість унікальних оцінок: {len(uniques)}")