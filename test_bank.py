from amount import Amount

from personalAccount import PersonalAccount

account = PersonalAccount(1303030,"Said Z", 5000, [])

account.deposit(100.0)
account.withdraw(1000.0)
account.print_transaction_history()

print(account)