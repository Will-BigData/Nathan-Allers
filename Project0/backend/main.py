from controller.controller import app, load_account_service
from DAO.account_DAO import AccountDAO
import tomllib
import os

with open("backend/config.toml", "rb") as f:
    data = tomllib.load(f)
    load_account_service(data["accounts_file_path"])

app.run()
