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

#Класс еды
class Food(GameObject):
    def __init__(self, image):
        GameObject.__init__(self)
        self._object = image
        self.x = 0
        self.y = 0
        self._width = image.get_width()
        self._height = image.get_height()
        self._saturation = 0

    @property
    def saturation(self):
        return self._saturation

    @saturation.setter
    def saturation(self, level):
        self._saturation = level