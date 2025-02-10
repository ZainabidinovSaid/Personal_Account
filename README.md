# Personal Account Management System

This project implements a simple **Personal Account Management System** in Python. It allows users to:
- Deposit money into an account
- Withdraw money from an account
- View transaction history
- Check account balance

## Classes and Structure
### 1. `Amount`
Represents a transaction (deposit or withdrawal) with an amount, timestamp, and transaction type.

#### Methods:
- `__init__(amount, transaction_type)`: Initializes a new transaction with the specified amount and type.
- `__str__()`: Returns a string representation of the transaction.

### 2. `PersonalAccount`
Handles account details, transactions, and balance management.

#### Attributes:
- `account_number`: The unique account number.
- `account_holder`: The name of the account holder.
- `balance`: The current balance of the account.
- `transactions`: A list of all transactions.

#### Methods:
- `__init__(account_number, account_holder, balance, transactions)`: Initializes an account.
- `deposit(amount)`: Adds the specified amount to the balance and records the transaction.
- `withdraw(amount)`: Deducts the specified amount from the balance if funds are sufficient.
- `print_transaction_history()`: Displays all recorded transactions.
- `get_balance()`: Returns the current balance.
- `get_account_number()`: Returns the account number.
- `set_account_number(account_number)`: Sets a new account number.
- `get_account_holder()`: Returns the account holder's name.
- `set_account_holder(account_holder)`: Sets a new account holder's name.
- `__str__()`: Returns a string representation of the account.
- `__add__(amount)`: Allows deposits using the `+` operator.
- `__sub__(amount)`: Allows withdrawals using the `-` operator.

![Диаграмма без названия](https://github.com/user-attachments/assets/260673f0-bfdb-4e31-af29-f5bfb5da6bfe)

Tests:

![Снимок экрана (134)](https://github.com/user-attachments/assets/00dc3964-083c-4e81-aa9a-e7ff20e7b5ef)

