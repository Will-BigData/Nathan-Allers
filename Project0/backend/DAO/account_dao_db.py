from common.model import Account
from .account_dao import AccountDAO
from sqlalchemy import text

class AccountDAO_DB(AccountDAO):
    def __init__(self, engine):
        self._engine = engine

    def get_account_by_number(self, account_number: int) -> Account | None:
        with self._engine.begin() as connection:
            query = text("select account_number, routing_number, balance from accounts where account_number = :x")
            result = connection.execute(query, {"x": account_number})
            row = result.one_or_none()
            if row is not None:
                return Account(row.account_number, row.routing_number, row.balance)
        return None
    
    def get_all_accounts(self) -> list:
        with self._engine.begin() as connection:
            query = text("select account_number, routing_number, balance from accounts")
            result = connection.execute(query)
            li = [Account(row.account_number, row.routing_number, row.balance) for row in result]
            return li
    
    def insert_account(self, account: Account):
        with self._engine.begin() as connection:
            query = text("insert into accounts(account_number, routing_number, balance) values (:acc, :rou, :bal)")
            connection.execute(query, {"acc": account.get_account_number(), "rou": account.get_routing_number(), "bal": account.get_balance()})