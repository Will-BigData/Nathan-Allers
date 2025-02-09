import os
from sqlalchemy import create_engine, URL
from common.config import ConfigManager
from common.util import handle_with_message

class EngineManager:
    _engine = None

    @handle_with_message(KeyError, "[ERROR] Database config invalid")
    def get_engine():
        if EngineManager._engine is None:
            db_config = ConfigManager.get_config("backend", "database")
            dialect = db_config["dialect"]
            driver = db_config["driver"]
            url = URL.create(
                dialect + '+' + driver,
                username=os.environ[db_config["username_env_var"]],
                password=os.environ[db_config["password_env_var"]],
                host=db_config["host"],
                port=int(db_config["port"]),
                database=db_config["name"]
            )
            EngineManager._engine = create_engine(url)
        return EngineManager._engine