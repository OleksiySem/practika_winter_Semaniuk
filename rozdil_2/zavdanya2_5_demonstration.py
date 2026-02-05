from rozdil_2.zavdanya2_5_bankaccount import BankAccount

my_account = BankAccount(1000)

print("--- Робота через методи ---")
my_account.deposit(500)      # Баланс стане 1500
my_account.withdraw(200)     # Баланс стане 1300
my_account.withdraw(5000)    # Спроба зняти більше, ніж є (буде відмовлено)

print(f"Перевірка балансу через get_balance(): {my_account.get_balance()} грн.")

# Спроба прямого доступу до приватного атрибуту
print("\n--- Спроба зламати інкапсуляцію ---")
try:
    print(my_account.__balance)
except AttributeError as e:
    print(f"ПОМИЛКА ДОСТУПУ: {e}")

try:
    # Намагаємося змінити баланс напряму
    my_account.__balance = 1000000
    # Python дозволить створити нову змінну з таким ім'ям в об'єкті,
    # але це НЕ вплине на справжній внутрішній баланс класу.
    print(f"Створено нову змінну '__balance', але реальний баланс: {my_account.get_balance()} грн.")
except Exception as e:
    print(e)