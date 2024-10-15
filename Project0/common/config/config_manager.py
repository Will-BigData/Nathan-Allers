import tomllib
from common.util import handle_with_message

class ConfigManager:
    _data = None
    
    @handle_with_message(KeyError, "Invalid configuration")
    def get_config(*args):
        if ConfigManager._data is None:
            with open("config.toml", "rb") as f:
                ConfigManager._data = tomllib.load(f)

        def index(d: dict, *keys):
            result = d[keys[0]]
            if isinstance(result, dict) and len(keys) > 1:
                return index(result, *keys[1:])
            return result

        return index(ConfigManager._data, *args)