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
