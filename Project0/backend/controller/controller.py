from flask import Flask
from service.account_service import AccountService

app: Flask = Flask(__name__)
account_service = None

def load_account_service(account_file_path: str):
    global account_service
    account_service = AccountService(account_file_path)

@app.get("/")
def index():
    return "index"

@app.get("/accounts/<account_number>")
def get_account_by_number(account_number: str):
    return str(account_service.get_account_by_number(int(account_number)))

if __name__ == "__main__":
    app.run()