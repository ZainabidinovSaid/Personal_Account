from datetime import datetime

class Amount:
    def __init__(self, amount, transaction_type):
        self.amount = float(amount)
        self.timestamp = datetime.now()
        self.transaction_type = transaction_type

    def __str__(self):
        return f"{self.transaction_type}: ${self.amount:.2f} on {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"