import os
from configparser import ConfigParser

print(os.getcwd())
print(os.path.dirname(os.getcwd()))
config = ConfigParser()
config.read(os.path.dirname(os.getcwd()) + "\\testbed\\userdetails.ini")
print(config.get('basic', 'a'))
