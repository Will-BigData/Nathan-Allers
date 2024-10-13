from flask import Flask, request
from backend.service import AccountService
from common.config import ConfigManager
from backend.DAO import AccountDAOFactory
from common.model import Account

app: Flask = Flask(__name__)
account_service = AccountService(AccountDAOFactory.get_dao_by_type(ConfigManager.get_config("backend", "account_dao_type")))

@app.get("/")
def index():
    return "index"

@app.get("/accounts/<account_number>")
def get_account_by_number(account_number: str):
    try:
        account = account_service.get_account_by_number(int(account_number))
        if account is not None:
            return vars(account)
        return "No account exists with account number " + account_number, 404
    except ValueError:
        return 'Invalid request', 400

@app.get("/accounts")
def get_all_accounts():
    accounts = account_service.get_all_accounts()
    return list(map(vars, accounts))

@app.post("/accounts")
def add_new_account():
    account = Account(**request.get_json())
    if not account_service.insert_account(account):
        return "Account number already exists", 400
    return "Account added"

if __name__ == "__main__":
    app.run()