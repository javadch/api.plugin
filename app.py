import flask
from config.configManager import ConfigManager
from core.pluginManager import PluginManager
from configparser import ConfigParser
from utils.util import AttrDict

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#ini_config = ConfigParser(dict_type=AttrDict)
ini_config = ConfigParser()
ini_config.read('app.ini')

def basePath():
    return "/" + ini_config['API']['path'] + "/" + ini_config['API']['version'] + "/"

def installPlugins():
    # get the list of plugins from the config
    configManager = ConfigManager()
    plugins= configManager.get_active_plugins()

    print("Loading plugins ...")
    print("-" * 20)

    pluginManager = PluginManager(plugins)
    pluginManager.load()
    pluginManager.register(basePath(), app)

    print("plugins loading completed.")
    print("-" * 20)


@app.route('/', methods=['GET'])
def home():
    return "<h1>System is Running</h1><p>This is the root path</p>"

installPlugins()
app.run()

