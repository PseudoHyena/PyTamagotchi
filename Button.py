import pygame
from GameObjects import GameObject

class Button(GameObject):
    def __init__(self, image, text, font, func):
        GameObject.__init__(self)
        self._object = image
        self._textObj = font.render(text, False, (0, 0, 0)).convert()
        self._func = func
        self.x = 0
        self.y = 0
        self._width = image.get_width()
        self._height = image.get_height()
        self.textX = (self._width - self._textObj.get_width()) // 2
        self.textY = (self._height - self._textObj.get_height()) // 2

    @property
    def text(self):
        return self._textObj

    @property
    def func(self):
        self._func()

