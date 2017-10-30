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

class Pet(GameObject):
    def __init__(self, image):
        GameObject.__init__(self)
        self._object = image
        self.x = 0
        self.y = 0
        self._width = image.get_width()
        self._height = image.get_height()
