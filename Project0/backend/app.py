import functools
from flask import Flask, request
from backend.service import AccountService
from common.config import ConfigManager
from backend.DAO import AccountDAOFactory
from common.model import Account
from common.util import handle_with_func

app: Flask = Flask(__name__)
account_service = AccountService(AccountDAOFactory.get_dao_by_type(ConfigManager.get_config("backend", "account_dao_type")))

handle_bad_path_parameter = handle_with_func(ValueError, lambda: ('Invalid request', 400))
handle_generic_error = handle_with_func(Exception, lambda: ('Internal server error', 500))

unknown_account_view = lambda account_number: (f"No account exists with account number {account_number}", 404)

@app.get("/")
def index():
    return "index"

@app.get("/accounts/<account_number>")
@handle_generic_error
@handle_bad_path_parameter
def get_account_by_number(account_number: str):
    account = account_service.get_account_by_number(int(account_number))
    if account is not None:
        return vars(account)
    return unknown_account_view(account_number)
    

@app.patch("/accounts/<account_number>")
@handle_generic_error
@handle_bad_path_parameter
def update_account_by_number(account_number: str):
    if account_service.update_account(int(account_number), Account(**request.get_json())):
        return "Account updated"
    return unknown_account_view(account_number)

@app.get("/accounts")
@handle_generic_error
def get_all_accounts():
    accounts = account_service.get_all_accounts()
    return list(map(vars, accounts))

@app.post("/accounts")
@handle_generic_error
def add_new_account():
    account = Account(**request.get_json())
    if not account_service.insert_account(account):
        return "Account number already exists", 400
    return "Account added"

@app.delete("/accounts/<account_number>")
@handle_generic_error
@handle_bad_path_parameter
def delete_account(account_number: str):
    if not account_service.delete_account(int(account_number)):
        return unknown_account_view(account_number)
    return "Account deleted"

def main():
    app.run()

if __name__ == "__main__":
    main()