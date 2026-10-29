
class BankAccount:
    account_counter = 1000

    def __init__(self, account_holder):
        BankAccount.account_counter += 1
        self.account_number = BankAccount.account_counter
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(amount, "deposited successfully")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount <= self.balance:
            self.balance -= amount
            print(amount, "withdrawn successfully")
        else:
            print("Insufficient balance")

    def display_balance(self):
        print("Account Number:", self.account_number)
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)

    def transfer(self, amount, other_account):
        if amount <= 0:
            print("Invalid transfer amount")
        elif amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print(amount, "transferred successfully")
        else:
            print("Insufficient balance for transfer")


a1 = BankAccount("Shreya")
a2 = BankAccount("Priya")

a1.deposit(5000)
a1.withdraw(1000)
a1.transfer(1500, a2)

print("\nAccount 1 Details:")
a1.display_balance()

print("\nAccount 2 Details:")
a2.display_balance()
