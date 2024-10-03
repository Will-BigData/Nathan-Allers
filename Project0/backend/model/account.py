class Account:
    def __init__(self, account_number, routing_number, balance):
        self._account_number = account_number
        self._routing_number = routing_number
        self._balance = balance

    def get_account_number(self) -> int:
        return self._account_number
    
    def set_account_number(self, account_number: int) -> bool:
        if account_number > 0:
            self._account_number = account_number
            return True
        return False
    
    def get_routing_number(self) -> int:
        return self._routing_number
    
    def set_routing_number(self, routing_number: int) -> bool:
        if routing_number > 0:
            self._account_number = routing_number
            return True
        return False
    
    def get_balance(self):
        return self._balance
    
    def deposit(self, amount: int) -> bool:
        if isinstance(amount, int):
            if amount > 0:
                self.balance += amount
                return True
        return False
    
    def __str__(self):
        return f"Account Number: {self.account_number}\nRouting Number: {self.routing_number}\nBalance: ${self.balance}"
    
    