class Account:
    def __init__(self, _account_number: int=None, _routing_number: int=None, _balance: int=None):
        self._account_number = _account_number
        self._routing_number = _routing_number
        self._balance = _balance

    def get_account_number(self) -> int | None:
        return self._account_number
    
    def set_account_number(self, account_number: int):
        self._account_number = account_number
    
    def get_routing_number(self) -> int | None:
        return self._routing_number
    
    def set_routing_number(self, routing_number: int):
        self._routing_number = routing_number
    
    def get_balance(self) -> int | None:
        return self._balance
    
    def set_balance(self, balance: int):
        self._balance = balance
    
    def __str__(self):
        return f"Account Number: {self._account_number}\nRouting Number: {self._routing_number}\nBalance: ${self._balance}"
    
    