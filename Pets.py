import pygame
from GameObjects import GameObject

#Класс гуся из заставки :)
class Goose(GameObject):
    def __init__(self, images, posX, posY):
        GameObject.__init__(self)
        self._object = images
        self.x = posX
        self.y = posY
        self._width = images[0].get_width()
        self._height = images[0].get_height()

#Класс питомцев
class Pet(GameObject):
    def __init__(self, images):
        GameObject.__init__(self)
        self._object = images
        self.x = 0
        self.y = 0
        self._width = images[0].get_width()
        self._height = images[0].get_height()
        self.hungerLevel = 0
        self.moodLevel = 0
