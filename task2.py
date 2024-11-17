# Создайте класс BankAccount, который имеет:

# Атрибут balance, начальное значение которого равно 0.

# Метод deposit(amount), который увеличивает баланс на
# сумму amount.

# Метод withdraw(amount), который уменьшает баланс на сумму
# amount, если на счете достаточно средств;
# если недостаточно, выведите сообщение "Недостаточно средств".

# Метод get_balance, который возвращает текущий баланс.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("Недостаточно средств")

    def get_balance(self):
        return self.balance


balance = BankAccount(100)
print(balance.get_balance())
balance.deposit(20)
balance.withdraw(90)
balance.withdraw(500)
print(balance.get_balance())