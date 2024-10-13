import json
from .account_dao import AccountDAO
from common.model import Account

class AccountDAO_JSON(AccountDAO):
    def __init__(self, accounts_file_path: str):
        self.accounts_file_path: str = accounts_file_path
        self._accounts: list[Account] = [Account(**account) for account in json.load(open(accounts_file_path))["accounts"]]
    
    def _write_after(func):
        def inner(self, *args):
            func(self, *args)
            self.write_json()
        return inner
    
    def get_account_by_number(self, account_number: int) -> Account:
        for account in self._accounts:
            if account.get_account_number() == account_number:
                return account
        return None
    
    def get_all_accounts(self) -> list:
        return self._accounts[:]
    
    @_write_after
    def insert_account(self, account: Account):
        self._accounts.append(account)

    def write_json(self):
        json.dump({"accounts": [vars(account) for account in self._accounts]}, open(self.accounts_file_path, "w"), indent=4)