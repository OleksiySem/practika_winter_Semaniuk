class BankAccount:
    def __init__(self, initial_balance: float = 0):
        self.__balance = None
        if initial_balance < 0:
            print("Початковий баланс не може бути від'ємним. Встановлено 0.")
            self.__balance = 0.0
        else:
            self.__balance = float(initial_balance)

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            print(f"Поповнено на: {amount} грн. Поточний баланс: {self.__balance} грн.")
        else:
            print("Сума поповнення повинна бути додатною.")

    def withdraw(self, amount: float):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Знято: {amount} грн. Поточний баланс: {self.__balance} грн.")
            else:
                print(f"Помилка: Недостатньо коштів. Ваш баланс: {self.__balance} грн.")
        else:
            print("Сума зняття повинна бути додатною.")

    def get_balance(self) -> float:
        return self.__balance

