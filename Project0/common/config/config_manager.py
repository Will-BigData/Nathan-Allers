import tomllib

class ConfigManager:
    _data = None
        
    def get_config(*args):
        if ConfigManager._data is None:
            with open("./common/config/config.toml", "rb") as f:
                ConfigManager._data = tomllib.load(f)
            
        def index(d: dict, *keys):
            result = d[keys[0]]
            if isinstance(result, dict) and len(keys) > 1:
                return index(result, *keys[1:])
            return result

        return index(ConfigManager._data, *args)