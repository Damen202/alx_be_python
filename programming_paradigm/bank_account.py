class BankAccount:
    def __init__(self, account_balance=0):
        self.balance = account_balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount:.2f}")
            return True
        else:
            #print("Insufficient funds or invalid withdrawal amount.")
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")
