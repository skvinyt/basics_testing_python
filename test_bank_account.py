class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds")
        elif amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance

# Тесты
import pytest

def test_initial_balance():
    account = BankAccount(100)
    assert account.get_balance() == 100

def test_deposit():
    account = BankAccount(100)
    account.deposit(50)
    assert account.get_balance() == 150

def test_withdraw():
    account = BankAccount(100)
    account.withdraw(50)
    assert account.get_balance() == 50

def test_withdraw_insufficient_funds():
    account = BankAccount(100)
    with pytest.raises(InsufficientFundsError):
        account.withdraw(150)

def test_default_initial_balance():
    account = BankAccount()
    assert account.get_balance() == 0

def test_deposit_negative_amount():
    account = BankAccount(100)
    with pytest.raises(ValueError):
        account.deposit(-50)

def test_withdraw_negative_amount():
    account = BankAccount(100)
    with pytest.raises(ValueError):
        account.withdraw(-50)

# Запуск тестов
if __name__ == "__main__":
    pytest.main()
