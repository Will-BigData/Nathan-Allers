from common.model import Account
from .account_dao import AccountDAO
from sqlalchemy import text, Engine, exc
from common.util import reraise_with_message

handle_operational_error = reraise_with_message(exc.OperationalError, "[ERROR] Database operation failed")
handle_bad_engine = reraise_with_message(AttributeError, "[ERROR] Bad database engine")

class AccountDAO_DB(AccountDAO):
    def __init__(self, engine: Engine):
        self._engine = engine
    
    @handle_operational_error
    @handle_bad_engine
    def get_account_by_number(self, account_number: int) -> Account | None:
        with self._engine.begin() as connection:
            query = text("select account_number, routing_number, balance from accounts where account_number = :acc")
            result = connection.execute(query, {"acc": account_number})
            row = result.one_or_none()
            if row is not None:
                return Account(row.account_number, row.routing_number, row.balance)
        return None
    
    @handle_operational_error
    @handle_bad_engine
    def get_all_accounts(self) -> list[Account]:
        with self._engine.begin() as connection:
            query = text("select account_number, routing_number, balance from accounts")
            result = connection.execute(query)
            li = [Account(row.account_number, row.routing_number, row.balance) for row in result]
            return li
    
    @handle_operational_error
    @handle_bad_engine
    def insert_account(self, account: Account):
        with self._engine.begin() as connection:
            query = text("insert into accounts(account_number, routing_number, balance) values (:acc, :rou, :bal)")
            connection.execute(query, {"acc": account.get_account_number(), "rou": account.get_routing_number(), "bal": account.get_balance()})
    
    @handle_operational_error
    @handle_bad_engine
    def update_account(self, account_number: int, account: Account):
        existing_account = self.get_account_by_number(account_number)
        if existing_account is not None:
            new_routing_number = account.get_routing_number()
            new_balance = account.get_balance()
            with self._engine.begin() as connection:
                if new_routing_number is not None:
                    query = text("update accounts set routing_number = :rou where account_number = :acc")
                    connection.execute(query, {"rou": new_routing_number, "acc": existing_account.get_account_number()})
                if new_balance is not None:
                    query = text("update accounts set balance = :bal where account_number = :acc")
                    connection.execute(query, {"bal": new_balance, "acc": existing_account.get_account_number()})
    
    @handle_operational_error
    @handle_bad_engine
    def delete_account(self, account_number: int):
        with self._engine.begin() as connection:
            query = text("delete from accounts where account_number = :acc")
            connection.execute(query, {"acc": account_number})
                