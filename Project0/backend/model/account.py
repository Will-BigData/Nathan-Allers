import json

class Account:
    def __init__(self, account_number, routing_number, balance):
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance

    def deposit(self, amount: int):
        if isinstance(amount, int):
            if amount > 0:
                self.balance += amount
    
    def to_json(self) -> str:
        return json.dumps(vars(self))
    
    def __str__(self):
        return f"Account Number: {self.account_number}\nRouting Number: {self.routing_number}\nBalance: ${self.balance}"

if __name__ == "__main__":
    acc = Account(123, 456, 0)
    print(acc.to_json())
    