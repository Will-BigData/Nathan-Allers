import tomllib

class ConfigManager:
    _data = None
    def __init__(self):
        if ConfigManager._data is None:
            with open("backend/config/config.toml", "rb") as f:
                ConfigManager._data = tomllib.load(f)
    def get_config(self, key: str):
        return ConfigManager._data[key]