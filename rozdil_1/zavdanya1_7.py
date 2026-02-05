students = [
    {"prizv": "Петренко", "imya": "Олексій", "grades": [9, 10, 11, 7, 8]},
    {"prizv": "Іванова", "imya": "Марія", "grades": [8, 9, 9, 7, 10]},
    {"prizv": "Сидорчук", "imya": "Іван", "grades": [10, 10, 11, 10, 11]},
]

num_subjects = 5

print(f"{'Прізвище':<12} | {'Ім’я':<10} | {'Оцінки':<12} | {'Сер. бал'}")
print("-" * 55)

subject_totals = [0] * num_subjects

for s in students:

    avg_student = sum(s["grades"]) / num_subjects

    grades_str = " ".join(map(str, s["grades"]))
    print(f"{s['prizv']:<12} | {s['imya']:<10} | {grades_str:<12} | {avg_student:.2f}")

    for i in range(num_subjects):
        subject_totals[i] += s["grades"][i]

print("-" * 55)

avg_subjects = [total / len(students) for total in subject_totals]

print(f"{'СЕРЕДНЄ ПО ГРУПІ:':<25} | {' '.join(f'{x:.1f}' for x in avg_subjects) }")
