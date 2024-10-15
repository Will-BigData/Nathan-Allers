import json
from .account_dao import AccountDAO
from common.model import Account
from common.util import reraise_with_message

class AccountDAO_JSON(AccountDAO):
    @reraise_with_message(OSError, "[ERROR] Unable to load accounts JSON file")
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
    
    def get_all_accounts(self) -> list[Account]:
        return self._accounts[:]
    
    @_write_after
    def insert_account(self, account: Account):
        self._accounts.append(account)
    
    @_write_after
    def update_account(self, account_number: int, account: Account):
        new_routing_number = account.get_routing_number()
        new_balance = account.get_balance()
        for existing_account in self._accounts:
            if existing_account.get_account_number() == account_number:
                if new_routing_number is not None:
                    existing_account.set_routing_number(new_routing_number)
                if new_balance is not None:
                    existing_account.set_balance(new_balance)
                return
    
    @_write_after
    def delete_account(self, account_number: int):
        for account in self._accounts:
            if account.get_account_number() == account_number:
                self._accounts.remove(account)
                return

    def write_json(self):
        json.dump({"accounts": [vars(account) for account in self._accounts]}, open(self.accounts_file_path, "w"), indent=4)