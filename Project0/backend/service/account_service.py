from backend.DAO.account_dao import AccountDAO

class AccountService:
    def __init__(self, account_DAO):
        self.account_DAO: AccountDAO = account_DAO
    def get_account_by_number(self, account_number: int):
        return self.account_DAO.get_account_by_number(account_number)