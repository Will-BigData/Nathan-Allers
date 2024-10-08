from backend.DAO.account_dao import AccountDAO
from common.model import Account

class AccountService:
    def __init__(self, account_DAO):
        self.account_DAO: AccountDAO = account_DAO
    def get_account_by_number(self, account_number: int):
        return self.account_DAO.get_account_by_number(account_number)
    def insert_account(self, account: Account):
        self.account_DAO.insert_account(account)
    def get_all_accounts(self):
        return self.account_DAO.get_all_accounts()