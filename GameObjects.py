import pygame

#Основной класс игровых объектов, содержащий основные свойства объектов
class GameObject:
    def __init__(self):
        self.x = 0
        self.y = 0
        self._width = 0
        self._height = 0
        self._object = None

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def object(self):
        return self._object

class Poop(GameObject):
    def __init__(self, num):
        GameObject.__init__(self)
        self._object = None
        self.x = 0
        self.y = 0
        self._number = num

    def setImage(self, image):
        self._object = image
        self._width = image.get_width()
        self._height = image.get_height()

    @property
    def number(self):
        return self._number