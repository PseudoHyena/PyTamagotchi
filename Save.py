import xml.etree.cElementTree as ET
import os

class User:
    def __initFile(self, name):
        if (os.path.exists(name) == False):
            file = open(name, "w")
            file.write("<Session></Session>")
            file.close()

    def __checkAttr(self, name):
        if (self._xRoot.find("Time") == None):
            time_elem = ET.SubElement(self._xRoot, "Time")
            time_elem.text = "0"
            self._xTree.write(name)

        if (self._xRoot.find("Pet") == None):
            pet_elem = ET.SubElement(self._xRoot, "Pet")
            self._xTree.write(name)

        if (self._xTree.find("Pet").find("HungerLevel") == None):
            hungerLevel_elem = ET.SubElement(self._xRoot.find("Pet"), "HungerLevel")
            hungerLevel_elem.text = "0"
            self._xTree.write(name)

        if (self._xTree.find("Pet").find("MoodLevel") == None):
            moodLevel_elem = ET.SubElement(self._xRoot.find("Pet"), "MoodLevel")
            moodLevel_elem.text = "50"
            self._xTree.write(name)

    def __init__(self, name):
        self.__initFile(name)
        self._saveXml_file = os.path.join(name)
        self._xTree = ET.parse(self._saveXml_file)
        self._xRoot = self._xTree.getroot()
        self.__checkAttr(name)

    @property
    def tree(self):
        return self._xTree

    @property
    def root(self):
        return self._xRoot

    @property
    def file(self):
        return self._saveXml_file
        
