from amount import Amount
class PersonalAccount():

    def __init__(self, account_number=None, account_holder=None, balance=None, transactions=None):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.transactions = transactions

    def deposit(self, amount):
        transaction = Amount(amount, "Deposit")
        self.transactions.append(transaction)
        self.balance += amount
        print(f"Deposited {amount}, New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance < amount:
            print("Not enough funds")
            return
        transaction = Amount(amount, "Withdraw")
        self.transactions.append(transaction)
        self.balance -= amount
        print(f"Withdrawed {amount}, New balance: {self.balance}")


    def print_transaction_history(self):
        for transaction in self.transactions:
            print(f"{transaction.transaction_type}: {transaction.amount}")

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number):
        self.account_number = int(self.account_number)

    def get_account_holder(self):
        return self.account_holder

    def set_account_holder(self, account_holder):
        self.account_holder = str(input("Please enter your account holder: "))

    def __str__(self):
        return f"bank account number: {self.account_number}, account holder: {self.account_holder}, balance: {self.balance}"

    def __add__(self, amount):
        self.deposit(amount)
        return self

    def __sub__(self, amount):
        self.withdraw(amount)
        return self