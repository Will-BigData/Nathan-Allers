from .account_dao import AccountDAO
from common.model import Account

class AccountDAOMock(AccountDAO):
    def __init__(self):
        self.accounts = [
            Account(123, 456, 0),
            Account(234, 567, 12345)
        ]
    def get_account_by_number(self, account_number: int) -> (Account | None):
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account
        return None
    def get_all_accounts(self) -> list:
        return self.accounts[:]
    
    def insert_account(self, account: Account):
        self.accounts.append(account)
