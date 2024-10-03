import json
from .account_dao import AccountDAO
from model.account import Account

class AccountDAO_JSON(AccountDAO):
    def __init__(self, accounts_file_path: str):
        self.accounts_file_path: str = accounts_file_path
        self.accounts: list = json.load(open(self.accounts_file_path))["accounts"]
    
    def get_account_by_number(self, account_number: int) -> Account:
        result = None
        for account in self.accounts:
            if account["accountNumber"] == account_number:
                result = Account(account_number, account["routingNumber"], account["balance"])
                break
        return result
    
    def get_all_accounts(self) -> list:
        return self.accounts