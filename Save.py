import xml.etree.cElementTree as ET
import os
from GameObjects import Poop

#Класс для работы с пользователем
class User:
    def __initFile(self, name):
        if (os.path.exists(name) == False):
            self._isFirstInit = True
            file = open(name, "w")
            file.write("<Session></Session>")
            file.close()

    def __checkAttr(self, name):
        if (self._xRoot.find("Time") == None):
            time_elem = ET.SubElement(self._xRoot, "Time")
            time_elem.text = "360"
            self._xTree.write(name)

        if (self._xRoot.find("Day") == None):
            day_elem = ET.SubElement(self._xRoot, "Day")
            day_elem.text = "0"
            self._xTree.write(name)

        if (self._xRoot.find("Poops") == None):
            day_elem = ET.SubElement(self._xRoot, "Poops")
            self._xTree.write(name)

        if (self._xRoot.find("Pet") == None):
            pet_elem = ET.SubElement(self._xRoot, "Pet")
            pet_elem.set("object", "None")
            self._xTree.write(name)

        if (self._xTree.find("Pet").find("HungerLevel") == None):
            hungerLevel_elem = ET.SubElement(self._xRoot.find("Pet"), "HungerLevel")
            hungerLevel_elem.text = "0"
            self._xTree.write(name)

        if (self._xTree.find("Pet").find("HungerDeathTik") == None):
            hungerDeathTik_elem = ET.SubElement(self._xRoot.find("Pet"), "HungerDeathTik")
            hungerDeathTik_elem.text = "0"
            self._xTree.write(name)

        if (self._xTree.find("Pet").find("MoodLevel") == None):
            moodLevel_elem = ET.SubElement(self._xRoot.find("Pet"), "MoodLevel")
            moodLevel_elem.text = "50"
            self._xTree.write(name)

        if (self._xTree.find("Pet").find("PoopHeap") == None):
            poopHeap_elem = ET.SubElement(self._xRoot.find("Pet"), "PoopHeap")
            poopHeap_elem.text = ""
            self._xTree.write(name)

    def __init__(self, name):
        self.__initFile(name)
        self._saveXml_file = os.path.join(name)
        self._xTree = ET.parse(self._saveXml_file)
        self._xRoot = self._xTree.getroot()
        self.__checkAttr(name)
        self._name = name
        self._petNumber = None if self._xRoot.find("Pet").attrib["object"] == "None" else \
            int(self._xRoot.find("Pet").attrib["object"])
        self._images = []

    def setImages(self, img1, img2):
        if (len(self._images) != 0):
            self._images.clear()

        self._images.append(img1)
        self._images.append(img2)

    def setPetNumber(self, num):
        self._petNumber = num

        self._xRoot.find("Pet").attrib["object"] = str(num)
        self._xTree.write(self._name)

    @property
    def tree(self):
        return self._xTree

    @property
    def root(self):
        return self._xRoot

    @property
    def file(self):
        return self._saveXml_file

    @property
    def hungerLevel(self):
        return int(self._xTree.find("Pet").find("HungerLevel").text)

    @hungerLevel.setter
    def hungerLevel(self, level):
        self._xTree.find("Pet").find("HungerLevel").text = str(level)
        self._xTree.write(self._name)

    @property
    def hungerDeathTik(self):
        return int(self._xTree.find("Pet").find("HungerDeathTik").text)

    @hungerDeathTik.setter
    def hungerDeathTik(self, num):
        self._xTree.find("Pet").find("HungerDeathTik").text = str(num)
        self._xTree.write(self._name)

    @property
    def moodLevel(self):
        return int(self._xTree.find("Pet").find("MoodLevel").text)

    @moodLevel.setter
    def moodLevel(self, level):
        self._xTree.find("Pet").find("MoodLevel").text = str(level)
        self._xTree.write(self._name)

    @property
    def poopHeap(self):
        return self._xTree.find("Pet").find("PoopHeap").text

    @poopHeap.setter
    def poopHeap(self, heap):
        self._xTree.find("Pet").find("PoopHeap").text = heap
        self._xTree.write(self._name)

    @property
    def time(self):
        return int(self._xRoot.find("Time").text)

    @time.setter
    def time(self, curTime):
        self._xRoot.find("Time").text = str(curTime)
        self._xTree.write(self._name)

    @property
    def day(self):
        return int(self._xRoot.find("Day").text)

    @day.setter
    def day(self, day):
        self._xRoot.find("Day").text = str(day)
        self._xTree.write(self._name)

    def getPoopsObjects(self):
        heap = []
        for elem in self._xRoot.find("Poops").findall("poop"):
            num = int(elem.attrib["num"])
            x = int(elem.attrib["x"])
            y = int(elem.attrib["y"])

            poop = Poop(num)
            poop.x = x
            poop.y = y
            heap.append(poop)

        return heap

    def setPoopsObject(self, heap):
        for elem in self._xRoot.find("Poops").findall("poop"):
            self._xRoot.find("Poops").remove(elem)

        self._xTree.write(self._name)
        
        for poop in heap:
            poop_elem = ET.SubElement(self._xTree.find("Poops"), "poop")
            poop_elem.set("num", str(poop.number))
            poop_elem.set("x", str(poop.x))
            poop_elem.set("y", str(poop.y))

        self._xTree.write(self._name)

    @property
    def pet_number(self):
        return self._petNumber

    @property
    def images(self):
        return self._images
        
