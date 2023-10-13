class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of ${amount} successful")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrawal of ${amount} successful")

    def display_balance(self):
        print(f"Your balance is ${self.balance}")


john = BankAccount("John", "Doe", "12345", "Checking", "1234", 1000)
jane = BankAccount("Jane", "Doe", "23456", "Savings", "5678", 2000)

jane.deposit(96)
jane.withdraw(25)
jane.display_balance()
