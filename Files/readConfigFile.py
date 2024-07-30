from configparser import ConfigParser

config = ConfigParser()

config.read("..//Files//Config.cfg")
print(config.get("section1", "username"))
