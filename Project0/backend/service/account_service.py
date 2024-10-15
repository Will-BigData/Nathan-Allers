from backend.DAO.account_dao import AccountDAO
from common.model import Account

class AccountService:
    def __init__(self, account_DAO):
        self.account_DAO: AccountDAO = account_DAO
    def get_account_by_number(self, account_number: int) -> Account | None:
        return self.account_DAO.get_account_by_number(account_number)
    def insert_account(self, account: Account) -> bool:
        if self.account_DAO.get_account_by_number(account.get_account_number()) is None:
            self.account_DAO.insert_account(account)
            return True
        return False
    def get_all_accounts(self) -> list[Account]:
        return self.account_DAO.get_all_accounts()
    def update_account(self, account_number: int, account: Account) -> bool:
        if self.get_account_by_number(account_number) is None:
            return False
        self.account_DAO.update_account(account_number, account)
        return True
    def delete_account(self, account_number: int):
        if self.get_account_by_number(account_number) is None:
            return False
        self.account_DAO.delete_account(account_number)
        return True
