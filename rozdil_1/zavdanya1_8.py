import pandas as pd

try:
    df = pd.read_csv('students.csv', encoding='utf-8')
except FileNotFoundError:
    print("Помилка: Файл students.csv не знайдено.")
    exit()

subject_columns = df.columns[2:]

df['Середній бал'] = df[subject_columns].mean(axis=1).round(2)

print("--- Таблиця успішності ---")

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
print(df)

group_means = df[subject_columns].mean().round(2)

print("\n--- Середній бал групи по предметах ---")
print(group_means)