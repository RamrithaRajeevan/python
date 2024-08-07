# design class BankAccount with attributes like account_number,balance &qwner_nmae. Define method to deposit,withdraw( with overdraft check), & display account information
class BankAccount:
    def __init__(self, account_number, balance, owner_name):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}.")
            else:
                print("Insufficient funds. Withdrawal denied.")
        else:
            print("Withdrawal amount must be positive.")

    def account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Owner Name: {self.owner_name}")
        print(f"Balance: ${self.balance}")


account = BankAccount("123456789", 16000, "John")
account.account_info()
account.deposit(500)
account.withdraw(200)
account.withdraw(6500)
account.account_info()
