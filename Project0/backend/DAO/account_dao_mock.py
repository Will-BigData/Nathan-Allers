from .account_dao import AccountDAO
from common.model import Account

class AccountDAOMock(AccountDAO):
    def __init__(self):
        self._accounts = [
            Account(123, 456, 0),
            Account(234, 567, 12345)
        ]
    def get_account_by_number(self, account_number: int) -> (Account | None):
        for account in self._accounts:
            if account.get_account_number() == account_number:
                return account
        return None
    def get_all_accounts(self) -> list[Account]:
        return self._accounts[:]
    
    def insert_account(self, account: Account):
        self._accounts.append(account)
    
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
    
    def delete_account(self, account_number: int):
        for account in self._accounts:
            if account.get_account_number() == account_number:
                self._accounts.remove(account)
                return
