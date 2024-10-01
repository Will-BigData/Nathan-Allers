import json
from model.account import Account

class AccountDAO:
    def __init__(self, accounts_file_path: str):
        self.accounts: list = json.load(open(accounts_file_path))["accounts"]
    
    def get_account_by_number(self, account_number: int):
        result = None
        for account in self.accounts:
            if account["accountNumber"] == account_number:
                result = Account(account_number, account["routingNumber"], account["balance"])
                break
        return result