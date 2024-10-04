from .account_dao_json import AccountDAO_JSON
from .account_dao_mock import AccountDAOMock
from backend.config import ConfigManager
from .account_dao import AccountDAO

class AccountDAOFactory:
    def get_json_dao() -> AccountDAO:
        return AccountDAO_JSON(ConfigManager().get_config("accounts_json_file"))
    def get_mock_dao() -> AccountDAO:
        return AccountDAOMock()
    def get_dao_by_type(dao_type: str) -> AccountDAO:
        if dao_type.lower() == "mock":
            return AccountDAOFactory.get_mock_dao()
        elif dao_type.lower() == "json":
            return AccountDAOFactory.get_json_dao()