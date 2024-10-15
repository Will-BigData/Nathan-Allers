from .account_dao_json import AccountDAO_JSON
from .account_dao_mock import AccountDAOMock
from .account_dao_db import AccountDAO_DB
from backend.database import EngineManager
from common.config import ConfigManager
from .account_dao import AccountDAO
from common.util import handle_with_message

class AccountDAOFactory:
    @handle_with_message(OSError, "[ERROR] Loading JSON DAO failed")
    def get_json_dao() -> AccountDAO:
        return AccountDAO_JSON(ConfigManager.get_config("backend", "accounts_json_file"))
    def get_mock_dao() -> AccountDAO:
        return AccountDAOMock()
    def get_db_dao() -> AccountDAO:
        return AccountDAO_DB(EngineManager.get_engine())
    def get_dao_by_type(dao_type: str) -> AccountDAO:
        match dao_type.lower():
            case "mock":
                return AccountDAOFactory.get_mock_dao()
            case "json":
                return AccountDAOFactory.get_json_dao()
            case "db":
                return AccountDAOFactory.get_db_dao()
            