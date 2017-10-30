import xml.etree.cElementTree as ET
import os

class User:
    def __initFile(self, name):
        if (os.path.exists(name) == False):
            file = open(name, "w")
            file.close()

    def __init__(self, name):
        self.__initFile(name)
        
