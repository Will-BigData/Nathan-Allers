from abc import ABC, abstractmethod
from common.model import Account

class AccountDAO(ABC):
    @abstractmethod
    def get_account_by_number(self, account_number: int) -> Account | None:
        pass

    @abstractmethod
    def get_all_accounts(self) -> list[Account]:
        pass

    @abstractmethod
    def insert_account(self, account: Account):
        pass

    @abstractmethod
    def update_account(self, account_number: int, account: Account):
        pass

    @abstractmethod
    def delete_account(self, account_number: int):
        pass