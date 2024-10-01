from DAO.account_DAO import AccountDAO

class AccountService:
    def __init__(self, accounts_file_path: str):
        self.account_DAO: AccountDAO = AccountDAO(accounts_file_path)
    def get_account_by_number(self, account_number: int):
        return self.account_DAO.get_account_by_number(account_number)