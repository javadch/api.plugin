import yaml


class ConfigManager:

    def get_plugins(self):
        with open("./config/plugins.yaml") as file:
            cfg = yaml.safe_load(file)
        _plugins:list=[]
        _plugins = cfg['plugins']
        return _plugins

    def get_active_plugins(self):
        _plugins:list = []
        pl:list = self.get_plugins()
        for p in pl:
            if (bool(p['active']) == True):
                _plugins.append(p)
        return _plugins        