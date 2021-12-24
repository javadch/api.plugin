import importlib
from flask import Blueprint

class PluginManager:
    _plugins:dict = {}
    _pluginItems:list = []

    def __init__(self, pluginItems:list=[]):
        self._pluginItems = pluginItems

    def load(self):
        for pluginItem in self._pluginItems:
            pluginPackage = "plugins." + pluginItem['name']
            pluginPath = pluginPackage + ".routes"
            module = importlib.import_module(pluginPath, package = pluginPackage)
            #module = __import__(pluginPath, fromlist=['routes'])
            self._plugins[pluginItem['name']] = module

    def register(self, upperPath, app):
        for pluginItem in self._pluginItems:
            if pluginItem['name'] in self._plugins:
                prefix  = upperPath + pluginItem['prefix'] + "/"
                loadedModule = self._plugins[pluginItem['name']]
                for obj in vars(loadedModule).values():
                    if isinstance(obj, Blueprint):
                        app.register_blueprint(obj, url_prefix= prefix)                

    def unregister(self, upperPath, app, pluginName):
        pass