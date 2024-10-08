import json
from .account_dao import AccountDAO
from common.model import Account

class AccountDAO_JSON(AccountDAO):
    def __init__(self, accounts_file_path: str):
        self.accounts_file_path: str = accounts_file_path
        self.accounts: list = [Account(**account) for account in json.load(open(accounts_file_path))["accounts"]]
    
    def _write_after(func):
        def inner(self, *args):
            func(self, *args)
            self.write_json()
        return inner
    
    def get_account_by_number(self, account_number: int) -> Account:
        result = None
        for account in self.accounts:
            if account["accountNumber"] == account_number:
                result = Account(account_number, account["routingNumber"], account["balance"])
                break
        return result
    
    def get_all_accounts(self) -> list:
        return self.accounts[:]
    
    @_write_after
    def insert_account(self, account: Account):
        self.accounts.append(account)
    
    @_write_after
    

    def write_json(self):
        json.dump({"accounts": [vars(account) for account in self.accounts]}, open(self.accounts_file_path, "w"), indent=4)