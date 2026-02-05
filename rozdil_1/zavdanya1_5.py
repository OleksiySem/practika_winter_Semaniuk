def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def main():
    print("--- Програма сортування масиву ---")

    try:
        user_input = input("Введіть числа через пробіл: ")

        numbers = [float(x) for x in user_input.split()]

        if not numbers:
            print("Масив порожній. Нічого сортувати.")
            return

        print(f"\nПочатковий масив: {numbers}")

        sorted_numbers = bubble_sort(numbers)

        print(f"Відсортований масив: {sorted_numbers}")

    except ValueError:
        print("Помилка! Будь ласка, вводьте лише числа.")

if __name__ == "__main__":
    main()