from flask import Flask, request
from service.account_service import AccountService
from config.config_manager import ConfigManager
from DAO.account_dao_factory import AccountDAOFactory

app: Flask = Flask(__name__)
account_service = AccountService(AccountDAOFactory.get_dao_by_type(ConfigManager().get_config("account_dao_type")))

@app.get("/")
def index():
    return "index"

@app.get("/accounts/<account_number>")
def get_account_by_number(account_number: str):
    account = account_service.get_account_by_number(int(account_number))
    if account is not None:
        return vars(account)
    return '', 404

@app.post("/accounts")
def add_new_account():
    account = request.get_json()

if __name__ == "__main__":
    app.run()